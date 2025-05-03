import json
from datetime import datetime
from pathlib import Path
from typing import List

from chat2md.domain.entities.conversation import Conversation, Message
from chat2md.domain.repositories.conversation_repository import ConversationRepository


class JsonFileRepository(ConversationRepository):
    """Implementation of ConversationRepository for JSON file storage."""

    def load_conversations(self, source: Path) -> List[Conversation]:
        """Load conversations from a JSON file."""
        with open(source, "r", encoding="utf-8") as f:
            data = json.load(f)

        conversations = []
        raw_conversations = data.get("conversations", [])

        for convo in raw_conversations:
            title = convo.get("title", "")
            mapping = convo.get("mapping", {})

            if not mapping:
                continue

            messages = []
            model = ""

            # Extract messages from the mapping
            for node in mapping.values():
                if not isinstance(node, dict):
                    continue

                message_data = node.get("message", {})
                if not isinstance(message_data, dict):
                    continue

                # Extract message content
                content = message_data.get("content", {})
                if isinstance(content, dict):
                    content = content.get("parts", [""])[0]
                content = str(content).strip()

                if not content:
                    continue

                # Extract message metadata
                metadata = message_data.get("metadata", {})
                if isinstance(metadata, dict):
                    model = model or metadata.get("model_slug", "")

                # Create message entity
                message = Message(
                    author=message_data.get("author", {}).get("role", "unknown"),
                    content=content,
                    create_time=datetime.fromtimestamp(message_data.get("create_time", 0))
                    if message_data.get("create_time")
                    else None,
                    message_id=message_data.get("id", "")
                )
                messages.append(message)

            # Create conversation entity
            conversation = Conversation(
                title=title,
                messages=messages,
                id=convo.get("id", ""),
                create_time=datetime.fromtimestamp(convo.get("create_time", 0))
                if convo.get("create_time")
                else None,
                update_time=datetime.fromtimestamp(convo.get("update_time", 0))
                if convo.get("update_time")
                else None,
                model=model
            )
            conversations.append(conversation)

        return conversations

    def save_conversation(self, conversation: Conversation, destination: Path) -> None:
        """Save a conversation to a file.
        Note: This implementation assumes we're saving in markdown format.
        For actual JSON saving, we would need to implement the reverse mapping.
        """
        raise NotImplementedError(
            "Direct JSON saving not implemented. Use MarkdownConverter for saving conversations."
        )
