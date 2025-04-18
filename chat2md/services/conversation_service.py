from pathlib import Path
from chat2md.parsers.conversation_parser import parse_conversation_to_markdown


def process_all_conversations(conversations_json: dict, output_dir: Path, full_meta: bool = False):
    """
    Iterates through all conversations in the loaded JSON and generates a Markdown file per conversation.
    """
    conversations = conversations_json.get("conversations", [])

    for idx, convo in enumerate(conversations):
        title = convo.get("title") or f"conversation-{idx}"
        mapping = convo.get("mapping")
        if not mapping:
            continue

        # Sanitize filename: remove/replace unsafe characters
        filename = f"{title.strip().replace(' ', '_')}.md"
        output_path = output_dir / filename

        # Convert the conversation to Markdown
        markdown = parse_conversation_to_markdown(mapping, full_meta=full_meta)

        # Write the result to disk
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(markdown)
