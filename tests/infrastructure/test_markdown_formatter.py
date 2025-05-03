"""Tests for the DefaultMarkdownFormatter."""
from datetime import datetime

import pytest

from chat2md.domain.entities.conversation import Conversation, Message
from chat2md.infrastructure.formatters.markdown_formatter import DefaultMarkdownFormatter


@pytest.fixture
def formatter():
    """Create a DefaultMarkdownFormatter instance."""
    return DefaultMarkdownFormatter()


def test_basic_conversation(formatter):
    """Test basic conversation without metadata."""
    conversation = Conversation(
        title="Test Conversation",
        messages=[
            Message(author="user", content="Hello"),
            Message(author="assistant", content="Hi there!")
        ]
    )

    markdown = formatter.convert_to_markdown(conversation)
    expected = (
        "**User:**\n"
        "Hello\n"
        "\n"
        "**Assistant:**\n"
        "Hi there!\n"
    )
    assert markdown == expected


def test_full_metadata(formatter):
    """Test conversation with full metadata."""
    create_time = datetime(2024, 3, 20, 14, 30)
    update_time = datetime(2024, 3, 20, 14, 35)
    conversation = Conversation(
        title="Test Conversation",
        id="conv123",
        create_time=create_time,
        update_time=update_time,
        model="gpt-4",
        messages=[
            Message(
                author="user",
                content="Hello",
                create_time=create_time,
                message_id="msg1"
            ),
            Message(
                author="assistant",
                content="Hi there!",
                create_time=create_time,
                message_id="msg2"
            )
        ]
    )

    markdown = formatter.convert_to_markdown(conversation, include_metadata=True)
    expected = (
        "---\n"
        "title: 'Test Conversation'\n"
        "conversation_id: 'conv123'\n"
        "created: '2024-03-20 14:30:00'\n"
        "updated: '2024-03-20 14:35:00'\n"
        "model: 'gpt-4'\n"
        "---\n"
        "\n"
        "\n## 2024-03-20\n"
        "\n"
        "**[14:30] User:** (id: `msg1`):\n"
        "Hello\n"
        "\n"
        "**[14:30] Assistant:** (id: `msg2`):\n"
        "Hi there!\n"
    )
    assert markdown == expected


def test_code_block_detection(formatter):
    """Test code block detection and language detection."""
    conversation = Conversation(
        title="Code Example",
        messages=[
            Message(author="user", content="Here's some Python code:"),
            Message(
                author="assistant",
                content="def hello():\n    print('Hello, world!')\n\nhello()"
            ),
            Message(author="user", content="And some SQL:"),
            Message(
                author="assistant",
                content="SELECT * FROM users WHERE age > 18;"
            )
        ]
    )

    markdown = formatter.convert_to_markdown(conversation)
    expected = (
        "**User:**\n"
        "Here's some Python code:\n"
        "\n"
        "**Assistant:**\n"
        "```python\n"
        "def hello():\n"
        "    print('Hello, world!')\n"
        "\n"
        "hello()\n"
        "```\n"
        "\n"
        "**User:**\n"
        "And some SQL:\n"
        "\n"
        "**Assistant:**\n"
        "```sql\n"
        "SELECT * FROM users WHERE age > 18;\n"
        "```\n"
    )
    assert markdown == expected


def test_empty_messages(formatter):
    """Test handling of empty messages."""
    conversation = Conversation(
        title="Empty Messages",
        messages=[
            Message(author="user", content="Hello"),
            Message(author="assistant", content="   "),  # Empty after strip
            Message(author="user", content="\n\n"),  # Empty after strip
            Message(author="assistant", content="Goodbye")
        ]
    )

    markdown = formatter.convert_to_markdown(conversation)
    expected = (
        "**User:**\n"
        "Hello\n"
        "\n"
        "**Assistant:**\n"
        "Goodbye\n"
    )
    assert markdown == expected


def test_multiple_days(formatter):
    """Test messages spanning multiple days."""
    day1 = datetime(2024, 3, 20, 14, 30)
    day2 = datetime(2024, 3, 21, 9, 15)
    conversation = Conversation(
        title="Multiple Days",
        messages=[
            Message(
                author="user",
                content="Day 1 message",
                create_time=day1,
                message_id="msg1"
            ),
            Message(
                author="assistant",
                content="Day 1 response",
                create_time=day1,
                message_id="msg2"
            ),
            Message(
                author="user",
                content="Day 2 message",
                create_time=day2,
                message_id="msg3"
            )
        ]
    )

    markdown = formatter.convert_to_markdown(conversation, include_metadata=True)
    expected = (
        "---\n"
        "title: 'Multiple Days'\n"
        "conversation_id: ''\n"
        "created: ''\n"
        "updated: ''\n"
        "model: ''\n"
        "---\n"
        "\n"
        "\n## 2024-03-20\n"
        "\n"
        "**[14:30] User:** (id: `msg1`):\n"
        "Day 1 message\n"
        "\n"
        "**[14:30] Assistant:** (id: `msg2`):\n"
        "Day 1 response\n"
        "\n"
        "\n## 2024-03-21\n"
        "\n"
        "**[09:15] User:** (id: `msg3`):\n"
        "Day 2 message\n"
    )
    assert markdown == expected
