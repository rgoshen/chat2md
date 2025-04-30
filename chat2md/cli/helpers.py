from pathlib import Path


def prepare_output_directory(json_path):
    """
    Create the output directory for Markdown files

    Args:
        json_path (Path): Path to the input JSON file

    Returns:
        Path: Path to the output directory
    """
    output_dir = json_path.parent / "markdown_output"
    output_dir.mkdir(exist_ok=True)
    return output_dir


def add_user_name_to_conversations(conversations, user_name):
    """
    Add user's custom name to each conversation if provided

    Args:
        conversations (list): List of conversation objects
        user_name (str): Custom name for user messages

    Returns:
        list: Updated conversations list
    """
    if user_name:
        for convo in conversations:
            convo["user_name"] = user_name
    return conversations
