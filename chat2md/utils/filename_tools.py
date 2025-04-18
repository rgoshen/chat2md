import re

def sanitize_filename(title: str) -> str:
    """
    Sanitizes a conversation title to be safe for use as a filename.
    Replaces spaces with underscores and removes characters unsafe for most file systems.
    """
    # Remove characters that are invalid or problematic on Windows/macOS/Linux
    return re.sub(r'[\\/*?:"<>|!]', '', title).replace(' ', '_')
