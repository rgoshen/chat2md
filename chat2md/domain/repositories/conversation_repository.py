from abc import ABC, abstractmethod
from pathlib import Path
from typing import List

from chat2md.domain.entities.conversation import Conversation


class ConversationRepository(ABC):
    """Abstract interface for conversation storage operations."""

    @abstractmethod
    def load_conversations(self, source: Path) -> List[Conversation]:
        """Load conversations from a source."""
        pass

    @abstractmethod
    def save_conversation(self, conversation: Conversation, destination: Path) -> None:
        """Save a single conversation to the specified destination."""
        pass
