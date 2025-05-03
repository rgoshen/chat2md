from abc import ABC, abstractmethod

from chat2md.domain.entities.conversation import Conversation


class MarkdownConverter(ABC):
    """Interface for converting conversations to markdown format."""

    @abstractmethod
    def convert_to_markdown(
        self,
        conversation: Conversation,
        include_metadata: bool = False
    ) -> str:
        """Convert a conversation to markdown format."""
        pass
