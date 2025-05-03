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

    for node_id in mapping:
        node = mapping[node_id]
        message = node.get("message")
        if not message:
            continue

        author = message.get("author", {}).get("role", "unknown")
        content = message.get("content", {})
        if isinstance(content, dict):
            content = content.get("parts", [""])[0]
        content = str(content).strip()  # Convert to string and strip in one go
        create_time = message.get("create_time")
        msg_id = message.get("id", "")

        if not content:  # This will catch empty strings after stripping
            continue  # Skip blank messages

        # Insert date heading if this is the first message or a new day
        if create_time and full_meta:
            dt = datetime.fromtimestamp(create_time)
            current_date = dt.strftime("%Y-%m-%d")
            current_time = dt.strftime("%H:%M")

            if last_date != current_date:
                output.append(f"\n## {current_date}\n")
                last_date = current_date

            # Include timestamp, author, and message ID
            output.append(f"**[{current_time}] {author.capitalize()}:** (id: `{msg_id}`):\n")
        else:
            # Only include author when not in full meta mode
            output.append(f"**{author.capitalize()}:**\n")

        # Format as code block if message is probably code
        if is_probably_code(content):
            language = detect_language(content)
            output.append(f"```{language}\n{content}\n```\n")
        else:
            output.append(content + "\n")

    return "\n".join(output)
