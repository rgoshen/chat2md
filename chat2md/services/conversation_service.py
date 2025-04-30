from pathlib import Path

from tqdm import tqdm

from chat2md.parsers.conversation_parser import parse_conversation_to_markdown
from chat2md.utils.filename_tools import sanitize_filename


def process_all_conversations(conversations_json: dict, output_dir: Path, full_meta: bool = False):
    """
    Orchestrates the processing of all conversations in the loaded JSON.
    Shows a progress bar during processing.

    Args:
        conversations_json (dict): The loaded conversations JSON
        output_dir (Path): Directory to write output markdown files
        full_meta (bool): Whether to include full metadata
    """
    conversations = conversations_json.get("conversations", [])

    # Create progress bar with dynamic width and no output buffering
    with tqdm(total=len(conversations), desc="Converting conversations", unit="file",
              dynamic_ncols=True, leave=True) as pbar:
        for idx, convo in enumerate(conversations):
            process_single_conversation(convo, idx, output_dir, full_meta)
            pbar.update(1)


def process_single_conversation(conversation: dict, idx: int, output_dir: Path, full_meta: bool = False):
    """
    Process a single conversation from JSON to Markdown

    Args:
        conversation (dict): Single conversation data
        idx (int): Index for fallback naming
        output_dir (Path): Output directory for markdown file
        full_meta (bool): Whether to include full metadata
    """
    title = conversation.get("title") or f"conversation-{idx}"
    mapping = conversation.get("mapping")

    if not mapping:
        return  # Skip conversations without messages

    # Generate output filename
    filename = generate_output_filename(title)
    output_path = output_dir / filename

    # Convert the conversation to Markdown
    markdown = parse_conversation_to_markdown(conversation, mapping, full_meta=full_meta)

    # Write to file
    write_markdown_to_file(output_path, markdown)


def generate_output_filename(title: str) -> str:
    """
    Generate a safe filename from the conversation title

    Args:
        title (str): The conversation title

    Returns:
        str: Sanitized filename with .md extension
    """
    return f"{sanitize_filename(title.strip())}.md"


def write_markdown_to_file(output_path: Path, markdown: str):
    """
    Write markdown content to a file

    Args:
        output_path (Path): Path to write the file to
        markdown (str): Markdown content to write
    """
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(markdown)
