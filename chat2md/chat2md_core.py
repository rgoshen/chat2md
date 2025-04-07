import json
import re
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
    return bool(re.search(
        r'[\n;{}()]')) or "def " in text or "class " in text or "import " in text


def format_message(author, time_str, content):
    author_name = "**Rick Goshen**" if author == "user" else "**ChatGPT**"
    if is_probably_code(content):
        lang = detect_language(content)
        return f"{author_name} [{time_str}]:\n```{lang}\n{content.strip()}\n```\n"
    else:
        return f"{author_name} [{time_str}]:\n{content.strip()}\n"


def parse_chat_json_to_markdown(json_path, output_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        chat_data = json.load(f)

    markdown_lines = []
    last_date = None

    for message in chat_data.get("messages", []):
        author = message.get("author", {}).get("role", "unknown")
        content = message.get("content", {}).get("parts", [""])[0]
        timestamp = message.get("create_time")

        if not timestamp:
            continue

        dt = datetime.fromtimestamp(timestamp)
        date_str = dt.strftime("%Y-%m-%d")
        display_date = dt.strftime("%B %d, %Y")
        time_str = dt.strftime("%H:%M:%S")

        if last_date != date_str:
            markdown_lines.append(f"\n---\n\n### Day Start: {display_date}\n")
            last_date = date_str

        formatted = format_message(author, time_str, content)
        markdown_lines.append(formatted)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(markdown_lines))

    print(f"✅ Syntax-highlighted Markdown created at: {output_path}")
