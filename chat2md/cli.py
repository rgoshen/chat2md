import argparse
from .chat2md_core import parse_chat_json_to_markdown


def main():
    parser = argparse.ArgumentParser(description="Convert ChatGPT conversations.json export to Markdown.")
    parser.add_argument("input", help="Path to the conversations.json file")
    parser.add_argument(
        "-f",
        "--full-meta",
        action="store_true",
        help="Include full metadata (YAML frontmatter, timestamps, message IDs)")
    args = parser.parse_args()

    parse_chat_json_to_markdown(args.input, full_meta=args.full_meta)
