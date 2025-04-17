import re
import json
from datetime import datetime
from chat2md.utils.text_tools import detect_language, is_probably_code

# === Main Entry Point: Parses ChatGPT-style JSON into Markdown ===


def parse_chat_json_to_markdown(json_path, full_meta=False):
    # Load the full ChatGPT conversation export file
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    output = []
    mapping = data["mapping"]  # Dictionary of messages keyed by node ID
    last_date = None  # Track the last date for inserting date headers

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

    # Print markdown to stdout (can be redirected to a file)
    print("\n".join(output))
