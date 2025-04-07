import argparse
from .chat2md_core import parse_chat_json_to_markdown


def main():
    parser = argparse.ArgumentParser(
        description="Convert ChatGPT-style JSON chat logs to Markdown.")
    parser.add_argument("input", help="Path to the JSON file")
    parser.add_argument("output", help="Path to save the Markdown output")
    args = parser.parse_args()
    parse_chat_json_to_markdown(args.input, args.output)
