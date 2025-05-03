from datetime import datetime
from chat2md.utils.text_tools import detect_language, is_probably_code

# === Parses a single ChatGPT conversation mapping into Markdown ===


def parse_conversation_to_markdown(mapping, full_meta=False, conversation_meta=None):
    output = []
    last_date = None

    # --- Add YAML frontmatter if full_meta and meta provided ---
    if full_meta and conversation_meta:
        frontmatter = [
            "---",
            f"title: '{conversation_meta.get('title', '')}'",
            f"conversation_id: '{conversation_meta.get('id', '')}'",
            f"created: '{conversation_meta.get('create_time', '')}'",
            f"updated: '{conversation_meta.get('update_time', '')}'",
            f"model: '{conversation_meta.get('model', '')}'",
            "---",
            ""
        ]
        output.extend(frontmatter)

    if not isinstance(mapping, dict):
        return "\n".join(output)

    for node_id in mapping:
        node = mapping[node_id]
        if not isinstance(node, dict):
            continue

        message = node.get("message")
        if not isinstance(message, dict):
            continue

        author = message.get("author", {})
        if not isinstance(author, dict):
            continue
        author_role = author.get("role", "unknown")

        content = message.get("content", {})
        if isinstance(content, dict):
            parts = content.get("parts", [""])
            content = parts[0] if parts else ""
        content = str(content).strip()  # Convert to string and strip in one go

        if not content:  # This will catch empty strings after stripping
            continue  # Skip blank messages

        create_time = message.get("create_time")
        msg_id = message.get("id", "")

        # Insert date heading if this is the first message or a new day
        if create_time and full_meta:
            try:
                dt = datetime.fromtimestamp(create_time)
                current_date = dt.strftime("%Y-%m-%d")
                current_time = dt.strftime("%H:%M")

                if last_date != current_date:
                    output.append(f"\n## {current_date}\n")
                    last_date = current_date

                # Include timestamp, author, and message ID
                output.append(f"**[{current_time}] {author_role.capitalize()}:** (id: `{msg_id}`):\n")
            except (TypeError, ValueError):
                # Fall back to non-timestamped format if datetime conversion fails
                output.append(f"**{author_role.capitalize()}:**\n")
        else:
            # Only include author when not in full meta mode
            output.append(f"**{author_role.capitalize()}:**\n")

        # Format as code block if message is probably code
        if is_probably_code(content):
            language = detect_language(content)
            output.append(f"```{language}\n{content}\n```\n")
        else:
            output.append(content + "\n")

    return "\n".join(output)
