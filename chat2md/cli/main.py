# === CLI Entry Point for chat2md ===
from pathlib import Path

from chat2md.adapters.filesystem import load_conversations_json
from chat2md.cli.helpers import prepare_output_directory, add_user_name_to_conversations
from chat2md.cli.parser import setup_argument_parser
from chat2md.services.conversation_service import process_all_conversations


def main():
    """
    Main entry point for the CLI application
    """
    # Parse command-line arguments
    parser = setup_argument_parser()
    args = parser.parse_args()

    # Convert input path to Path object
    json_path = Path(args.input)

    # Prepare output directory
    output_dir = prepare_output_directory(json_path)

    # Load conversations
    raw_conversations = load_conversations_json(json_path)

    # Add user name if provided
    raw_conversations = add_user_name_to_conversations(raw_conversations, args.user_name)

    # Process conversations
    conversations = {"conversations": raw_conversations}  # Wrap in expected structure
    process_all_conversations(conversations, output_dir, args.full_meta)


if __name__ == "__main__":
    main()
