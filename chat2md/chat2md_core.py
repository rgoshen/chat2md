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

# === Main Entry Point: Parses ChatGPT-style JSON into Markdown ===


def parse_chat_json_to_markdown(json_path, full_meta=False):
    with open(json_path, "r", encoding="utf-8") as f:
        # Load the full list of conversation objects from the JSON file
        data = json.load(f)

    # Loop through each conversation in the exported JSON
    for conv in data:
        # Extract title and sanitize for safe file naming
        # Remove unsafe characters and limit filename length
        title = conv.get("title", "Untitled")
        conv_id = conv.get("id", "")[:8]
        safe_title = re.sub(r'[^\w\s-]', '', title).strip()  # remove unsafe chars
        # Format filename as: <cleaned_title>_<conversation_id>.md
        filename = f"{'_'.join(safe_title.split())[:50]}_{conv_id}.md"

        created = datetime.utcfromtimestamp(conv.get("create_time", 0)).strftime("%Y-%m-%d %H:%M UTC")
        updated = datetime.utcfromtimestamp(conv.get("update_time", 0)).strftime("%Y-%m-%d %H:%M UTC")
        model = None

        messages = []
        for node_id, node in conv.get("mapping", {}).items():
            msg = node.get("message")
            if msg:
                model = model or msg.get("metadata", {}).get("model_slug")
                messages.append(msg)
        messages = sorted([m for m in messages if m.get("create_time")
                          is not None], key=lambda m: m["create_time"])

        # Collect all lines of the Markdown file for this conversation
        lines = []

        # If the --full-meta flag is set, prepend YAML frontmatter
        if full_meta:
            lines.append("---")
            lines.append(f'title: "{title}"')
            lines.append(f'conversation_id: "{conv.get("id", "")}"')
            lines.append(f'created: "{created}"')
            lines.append(f'updated: "{updated}"')
            if model:
                lines.append(f'model: "{model}"')
            lines.append("---\n")
        else:
            lines.append(f"# {title}\n")

        for msg in messages:
            role = msg.get("author", {}).get("role", "unknown")
            author = "**Rick Goshen**" if role == "user" else "**ChatGPT**"
            time_str = datetime.utcfromtimestamp(msg.get("create_time")).strftime("%Y-%m-%d %H:%M UTC")
            parts = msg.get("content", {}).get("parts", [""])
            if isinstance(parts, list) and parts and isinstance(parts[0], str):
                content = parts[0].strip()
            else:
                content = ""

            # If the --full-meta flag is set, prepend YAML frontmatter
            if full_meta:
                lines.append(f"### {author} ({time_str})")
                lines.append(f"<!-- msg_id: {msg.get('id')} -->")
            else:
                lines.append(f"{author} [{time_str}]:")

            if is_probably_code(content):
                lang = detect_language(content)
                lines.append(f"```{lang}\n{content}\n```")
            else:
                lines.append(content)

            lines.append("\n---\n")

        # Write the converted Markdown lines to the output file
        with open(filename, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        print(f"✅ Created: {filename}")
