import argparse
from .chat2md_core import parse_chat_json_to_markdown

def main():
    parser = argparse.ArgumentParser(description="Convert ChatGPT conversations.json export to Markdown.")
    parser.add_argument("input", help="Path to the conversations.json file")
    args = parser.parse_args()

    parse_chat_json_to_markdown(args.input)
