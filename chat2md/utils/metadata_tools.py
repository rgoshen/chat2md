def extract_model_info(mapping):
    """
    Extract model information from the first assistant message

    Args:
        mapping (dict): The message mapping containing the conversation content

    Returns:
        str: Model slug if found, empty string otherwise
    """
    for node_id in mapping:
        node = mapping[node_id]
        message = node.get("message", {})
        if message.get("author", {}).get("role") == "assistant":
            return message.get("metadata", {}).get("model_slug", "")
    return ""


def get_author_display_name(author_role, conversation):
    """
    Get the display name for an author based on their role

    Args:
        author_role (str): The role of the author (user, assistant, system)
        conversation (dict): The conversation object that may contain custom user name

    Returns:
        str: Display name for the author
    """
    # Map roles to proper display names
    author_display = {
        "user": "User",  # Default, will be replaced with custom name if available
        "assistant": "ChatGPT",
        "system": "System",
        "unknown": "Unknown"
    }.get(author_role, author_role.capitalize())

    # Use custom name for user if available
    if author_role == "user" and conversation.get("user_name"):
        author_display = conversation.get("user_name")

    return author_display
