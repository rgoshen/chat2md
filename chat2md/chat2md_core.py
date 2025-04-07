import re
import json
from datetime import datetime


def detect_language(text):
    text = text.strip()
    if text.startswith("{") or text.startswith("["):
        return "json"
    if "import java" in text or "public class" in text:
        return "java"
    if "def " in text or "import " in text or ":" in text:
        return "python"
    if "<html>" in text or "<!DOCTYPE html>" in text:
        return "html"
    if "SELECT" in text.upper() and "FROM" in text.upper():
        return "sql"
    if "function" in text or "=>" in text:
        return "javascript"
    return "text"


def is_probably_code(text):
    if not isinstance(text, str):
        return False
    return (
        bool(re.search(r'[\n;{}()]', text))
        or "def " in text
        or "class " in text
        or "import " in text
    )


def format_message(author, time_str, content):
    author_name = "**Rick Goshen**" if author == "user" else "**ChatGPT**"
    if not isinstance(content, str):
        content = str(content)
    if is_probably_code(content):
        lang = detect_language(content)
        return f"{author_name} [{time_str}]:\n```{lang}\n{content.strip()}\n```\n"
    else:
        return f"{author_name} [{time_str}]:\n{content.strip()}\n"


def extract_messages_from_mapping(mapping):
    messages = []
    for node_id, node in mapping.items():
        if node.get("message"):
            messages.append(node["message"])
    return sorted(
        [m for m in messages if m.get("create_time") is not None],
        key=lambda m: m["create_time"]
    )


def sanitize_filename(name):
    return re.sub(r'[\\/*?:"<>|]', "_", name).strip() or "Untitled"


def parse_chat_json_to_markdown(input_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        conversations = json.load(f)

    if not isinstance(conversations, list):
        raise ValueError("❌ Expected a ChatGPT export file (list of conversations).")

    for index, convo in enumerate(conversations, start=1):
        title = sanitize_filename(convo.get("title", "Untitled"))
        mapping = convo.get("mapping", {})
        messages = extract_messages_from_mapping(mapping)

        filename = f"{index:02d} - {title}.md"
        heading_title = re.sub(r'^\d+\s*-\s*', '', filename).replace('.md', '').strip()

        markdown_lines = []
        markdown_lines.append(f"# {heading_title}\n")
        last_date = None

        for message in messages:
            author = message.get("author", {}).get("role", "unknown")
            content_parts = message.get("content", {}).get("parts", [])
            content = content_parts[0] if content_parts else ""
            timestamp = message.get("create_time")

            if not content or not timestamp:
                continue

            dt = datetime.fromtimestamp(timestamp)
            date_str = dt.strftime("%Y-%m-%d")
            display_date = dt.strftime("%B %d, %Y")
            time_str = dt.strftime("%H:%M:%S")

            if last_date != date_str:
                markdown_lines.append(f"\n---\n\n### Day Start: {display_date}\n")
                last_date = date_str

            markdown_lines.append(format_message(author, time_str, content))

        with open(filename, 'w', encoding='utf-8') as out_file:
            out_file.write("\n".join(markdown_lines))

        print(f"✅ Created: {filename}")
