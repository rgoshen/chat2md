from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional


@dataclass
class Message:
    author: str
    content: str
    create_time: Optional[datetime] = None
    message_id: Optional[str] = None


@dataclass
class Conversation:
    title: str
    messages: List[Message]
    id: Optional[str] = None
    create_time: Optional[datetime] = None
    update_time: Optional[datetime] = None
    model: Optional[str] = None

    @property
    def is_empty(self) -> bool:
        return len(self.messages) == 0

    def add_message(self, message: Message) -> None:
        self.messages.append(message)
