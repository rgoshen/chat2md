import json
from pathlib import Path


def load_conversations_json(json_path: Path) -> dict:
    """
    Reads the full ChatGPT export JSON file and returns it as a dictionary.
    """
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)
