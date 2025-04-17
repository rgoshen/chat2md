# chat2md/utils/text_tools.py

import re

# Detect the programming or content language of a given text snippet.
# This is used for properly formatting code blocks in Markdown.
def detect_language(text):
    text = text.strip()
    checks = [
        ("json", lambda t: t.startswith("{") or t.startswith("[")),
        ("java", lambda t: "import java" in t or "public class" in t),
        ("python", lambda t: "def " in t or "import " in t or ":" in t),
        ("html", lambda t: "<html>" in t or "<!DOCTYPE html>" in t),
        ("sql", lambda t: "SELECT" in t.upper() and "FROM" in t.upper()),
        ("javascript", lambda t: "function" in t or "=>" in t),
    ]

    # Return the first matching language or default to 'text'
    return next((lang for lang, check in checks if check(text)), "text")

# Heuristic to determine if the given content is likely source code.
# Helps decide whether to wrap the content in a Markdown code block.
def is_probably_code(text):
    if not isinstance(text, str):
        return False

    # Check for common code indicators (newlines, braces, semicolons, etc.)
    return (
        bool(re.search(r'[\n;{}()]', text))
        or "def " in text
        or "class " in text
        or "import " in text
    )
