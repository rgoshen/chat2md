# === CLI Entry Point for chat2md ===
# This script provides a command-line interface to convert ChatGPT exports to Markdown.
import argparse
from .chat2md_core import parse_chat_json_to_markdown


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

    # Call the main processing function with the provided arguments
    parse_chat_json_to_markdown(args.input, full_meta=args.full_meta)
