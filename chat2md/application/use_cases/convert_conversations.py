import logging
import re
from pathlib import Path
from typing import List

from chat2md.application.interfaces.markdown_converter import MarkdownConverter
from chat2md.domain.exceptions import ConversationError, RepositoryError
from chat2md.domain.repositories.conversation_repository import ConversationRepository
from chat2md.infrastructure.config import Config


class ConvertConversationsUseCase:
    """Application use case for converting conversations to markdown."""

    def __init__(
        self,
        repository: ConversationRepository,
        markdown_converter: MarkdownConverter,
        config: Config
    ):
        self.repository = repository
        self.markdown_converter = markdown_converter
        self.config = config
        self.logger = logging.getLogger("chat2md")

    def execute(
        self,
        source_path: Path,
        output_dir: Path,
        include_metadata: bool = False
    ) -> List[Path]:
        """
        Execute the conversation conversion process.

        Args:
            source_path: Path to the source JSON file
            output_dir: Directory where markdown files will be saved
            include_metadata: Whether to include full metadata in the output

        Returns:
            List of paths to the generated markdown files

        Raises:
            ConversationError: If there is an error processing conversations
            RepositoryError: If there is an error accessing the repository
        """
        try:
            # Ensure output directory exists
            output_dir.mkdir(exist_ok=True)

            # Load conversations from source
            self.logger.info(f"Loading conversations from {source_path}")
            conversations = self.repository.load_conversations(source_path)
            self.logger.debug(f"Loaded {len(conversations)} conversations")

            # Convert each conversation and save to markdown
            output_files = []
            for conversation in conversations:
                if conversation.is_empty:
                    self.logger.warning(f"Skipping empty conversation: {conversation.title}")
                    continue

                try:
                    # Convert to markdown
                    self.logger.debug(f"Converting conversation: {conversation.title}")
                    markdown_content = self.markdown_converter.convert_to_markdown(
                        conversation,
                        include_metadata=include_metadata
                    )

                    # Generate output filename
                    safe_title = self._sanitize_filename(conversation.title or "untitled")
                    output_path = output_dir / f"{safe_title}.md"

                    # Save the markdown file
                    self.logger.debug(f"Saving to {output_path}")
                    with open(output_path, "w", encoding=self.config.encoding) as f:
                        f.write(markdown_content)

                    output_files.append(output_path)
                    self.logger.info(f"Successfully converted: {conversation.title}")

                except Exception as e:
                    self.logger.error(f"Error converting conversation {conversation.title}: {str(e)}")
                    raise ConversationError(f"Failed to convert conversation: {str(e)}") from e

            return output_files

        except Exception as e:
            self.logger.error(f"Error in conversion process: {str(e)}")
            raise RepositoryError(f"Failed to process conversations: {str(e)}") from e

    def _sanitize_filename(self, filename: str) -> str:
        """Convert a string to a safe filename."""
        # Replace spaces with underscores and remove unsafe characters
        return re.sub(r'[\\/*?:"<>|!]', '', filename).replace(' ', '_')
