from datetime import datetime
from chat2md.utils.text_tools import detect_language, is_probably_code

# === Parses a single ChatGPT conversation mapping into Markdown ===


def parse_conversation_to_markdown(mapping, full_meta=False):
    output = []
    last_date = None

    for node_id in mapping:
        node = mapping[node_id]
        message = node.get("message")
        if not message:
            continue

        author = message.get("author", {}).get("role", "unknown")
        content = message.get("content", {}).get("parts", [""])[0]
        create_time = message.get("create_time")

        if not content.strip():
            continue  # Skip blank messages

        # Insert date heading if this is the first message or a new day
        if create_time and full_meta:
            dt = datetime.fromtimestamp(create_time)
            current_date = dt.strftime("%Y-%m-%d")
            current_time = dt.strftime("%H:%M")

            if last_date != current_date:
                output.append(f"\n## {current_date}\n")
                last_date = current_date

            # Include timestamp with author name
            output.append(f"**[{current_time}] {author.capitalize()}:**\n")
        else:
            output.append(f"**{author.capitalize()}:**\n")

        # Format as code block if message is probably code
        if is_probably_code(content):
            language = detect_language(content)
            output.append(f"```{language}\n{content.strip()}\n```\n")
        else:
            output.append(content.strip() + "\n")

    return "\n".join(output)
