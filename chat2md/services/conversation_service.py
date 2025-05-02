from pathlib import Path
from tqdm import tqdm
from chat2md.parsers.conversation_parser import parse_conversation_to_markdown
from chat2md.utils.filename_tools import sanitize_filename


def process_all_conversations(conversations_json: dict, output_dir: Path, full_meta: bool = False):
    """
    Iterates through all conversations in the loaded JSON and generates a Markdown file per conversation.
    Shows a progress bar during processing.
    """
    conversations = conversations_json.get("conversations", [])

    # Create progress bar with dynamic width and no output buffering
    with tqdm(total=len(conversations), desc="Converting conversations", unit="file",
              dynamic_ncols=True, leave=True) as pbar:
        for idx, convo in enumerate(conversations):
            title = convo.get("title") or f"conversation-{idx}"
            mapping = convo.get("mapping")
            if not mapping:
                pbar.update(1)
                continue

            # Prepare meta for frontmatter
            conversation_meta = None
            if full_meta:
                # Extract model from first message that has it
                model = ""
                if mapping:
                    for msg in mapping.values():
                        if not isinstance(msg, dict):
                            continue
                        message = msg.get("message")
                        if not isinstance(message, dict):
                            continue
                        metadata = message.get("metadata")
                        if not isinstance(metadata, dict):
                            continue
                        model = metadata.get("model_slug", "")
                        if model:
                            break

                conversation_meta = {
                    "title": title,
                    "id": convo.get("id", ""),
                    "create_time": convo.get("create_time", ""),
                    "update_time": convo.get("update_time", ""),
                    "model": model
                }

            # Sanitize filename: remove/replace unsafe characters
            filename = f"{sanitize_filename(title.strip())}.md"
            output_path = output_dir / filename

            # Convert the conversation to Markdown
            markdown = parse_conversation_to_markdown(mapping, full_meta=full_meta, conversation_meta=conversation_meta)

            # Write the result to disk (silently)
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(markdown)

            # Update progress bar
            pbar.update(1)
