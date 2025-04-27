# === CLI Entry Point for chat2md ===
# This script provides a command-line interface to convert ChatGPT exports to Markdown.
import argparse
from pathlib import Path
from chat2md.adapters.filesystem import load_conversations_json
from chat2md.services.conversation_service import process_all_conversations


def main():
    # Set up argument parser for command-line interface
    parser = argparse.ArgumentParser(description="Convert ChatGPT conversations.json export to Markdown.")
    parser.add_argument("input", help="Path to the conversations.json file")
    parser.add_argument(
        # Optional flag to include full metadata (YAML frontmatter, timestamps, message IDs)
        "-f",
        # Optional flag to include full metadata (YAML frontmatter, timestamps, message IDs)
        "--full-meta",
        action="store_true",
        help="Include full metadata (YAML frontmatter, timestamps, message IDs)")

    # Parse command-line arguments
    args = parser.parse_args()

    # Convert input path to Path object and create output directory
    json_path = Path(args.input)
    output_dir = json_path.parent / "markdown_output"
    output_dir.mkdir(exist_ok=True)

    # Load and process conversations
    raw_conversations = load_conversations_json(json_path)
    conversations = {"conversations": raw_conversations}  # Wrap in expected structure
    process_all_conversations(conversations, output_dir, args.full_meta)
