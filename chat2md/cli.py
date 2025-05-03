# === CLI Entry Point for chat2md ===
# This script provides a command-line interface to convert ChatGPT exports to Markdown.
import argparse
import logging
import sys
from pathlib import Path

from chat2md.application.use_cases.convert_conversations import ConvertConversationsUseCase
from chat2md.domain.exceptions import Chat2MDError
from chat2md.infrastructure.config import Config
from chat2md.infrastructure.formatters.markdown_formatter import DefaultMarkdownFormatter
from chat2md.infrastructure.logging import setup_logging
from chat2md.infrastructure.persistence.json_file_repository import JsonFileRepository


def main():
    """CLI entry point for chat2md."""
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Convert ChatGPT conversations.json export to Markdown."
    )
    parser.add_argument(
        "input",
        help="Path to the conversations.json file"
    )
    parser.add_argument(
        "-f",
        "--full-meta",
        action="store_true",
        help="Include full metadata (YAML frontmatter, timestamps, message IDs)"
    )
    parser.add_argument(
        "--config",
        type=Path,
        help="Path to configuration file"
    )
    parser.add_argument(
        "--log-file",
        type=Path,
        help="Path to log file"
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable verbose logging"
    )

    # Parse arguments
    args = parser.parse_args()

    # Load configuration
    config = Config.load_from_file(args.config)
    if args.verbose:
        config.log_level = "DEBUG"

    # Setup logging
    setup_logging(config, args.log_file)
    logger = logging.getLogger("chat2md")

    try:
        # Set up paths
        input_path = Path(args.input)
        output_dir = input_path.parent / config.default_output_dir

        # Initialize components
        repository = JsonFileRepository()
        markdown_converter = DefaultMarkdownFormatter()
        use_case = ConvertConversationsUseCase(repository, markdown_converter, config)

        # Execute conversion
        logger.info("Starting conversation conversion")
        output_files = use_case.execute(
            source_path=input_path,
            output_dir=output_dir,
            include_metadata=args.full_meta
        )
        logger.info(f"Successfully converted {len(output_files)} conversations")
        logger.info(f"Output directory: {output_dir}")

    except Chat2MDError as e:
        logger.error(str(e))
        return 1
    except Exception:  # Using wildcard since logger.exception() includes the error info
        logger.exception("Unexpected error occurred")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
