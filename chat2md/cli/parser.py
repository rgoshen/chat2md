import argparse


def setup_argument_parser():
    """
    Set up the command line argument parser with all available options

    Returns:
        argparse.ArgumentParser: Configured argument parser
    """
    parser = argparse.ArgumentParser(description="Convert ChatGPT conversations.json export to Markdown.")
    parser.add_argument("input", help="Path to the conversations.json file")
    parser.add_argument(
        "-f",
        "--full-meta",
        action="store_true",
        help="Include full metadata (YAML frontmatter, timestamps, message IDs)")
    parser.add_argument(
        "-u",
        "--user-name",
        type=str,
        help="Custom name to use for 'user' messages (default: User)")

    return parser
