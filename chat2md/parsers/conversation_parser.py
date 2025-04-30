from datetime import datetime

import yaml
from chat2md.utils.formatting_tools import format_timestamp
from chat2md.utils.metadata_tools import extract_model_info, get_author_display_name

from chat2md.utils.text_tools import format_message_content


def parse_conversation_to_markdown(conversation, mapping, full_meta=False):
    """
    Parse a ChatGPT conversation into Markdown format

    Args:
        conversation (dict): The full conversation object with metadata
        mapping (dict): The message mapping containing the conversation content
        full_meta (bool): Whether to include full metadata (YAML frontmatter, timestamps, etc.)

    Returns:
        str: Formatted markdown text
    """
    output = []

    # Add frontmatter if requested
    if full_meta:
        frontmatter = generate_frontmatter(conversation, mapping)
        output.append(frontmatter)

    # Process messages
    messages_markdown = process_messages(conversation, mapping, full_meta)
    output.append(messages_markdown)

    return "\n".join(output)


def generate_frontmatter(conversation, mapping):
    """
    Generate YAML frontmatter from conversation metadata

    Args:
        conversation (dict): The conversation object with metadata
        mapping (dict): The message mapping containing the conversation content

    Returns:
        str: YAML frontmatter as a string
    """
    frontmatter = {
        'title': conversation.get('title', 'Untitled Conversation'),
        'conversation_id': conversation.get('id', ''),
        'created': format_timestamp(conversation.get('create_time', 0)),
        'updated': format_timestamp(conversation.get('update_time', 0)),
    }

    # Try to find model information from the first assistant message
    model = extract_model_info(mapping)
    if model:
        frontmatter['model'] = model

    # Convert frontmatter to YAML
    yaml_frontmatter = yaml.dump(frontmatter, default_flow_style=False)
    return f"---\n{yaml_frontmatter}---\n"


def process_messages(conversation, mapping, full_meta):
    """
    Process all messages in the conversation into Markdown

    Args:
        conversation (dict): The conversation object with metadata
        mapping (dict): The message mapping containing the conversation content
        full_meta (bool): Whether to include full metadata

    Returns:
        str: Markdown representation of all messages
    """
    output = []
    last_date = None

    for node_id in mapping:
        node = mapping[node_id]
        message = node.get("message")
        if not message:
            continue

        author_role = message.get("author", {}).get("role", "unknown")
        author_display = get_author_display_name(author_role, conversation)

        content = message.get("content", {})
        if isinstance(content, dict):
            content = content.get("parts", [""])[0]
        content = str(content).strip()

        create_time = message.get("create_time")

        if not content:  # Skip empty messages
            continue

        # Handle date headers and format message with timestamps
        if create_time:
            dt = datetime.fromtimestamp(create_time)
            current_date = dt.strftime("%Y-%m-%d")
            current_time = dt.strftime("%H:%M:%S")

            # Add day header if this is a new day
            if last_date != current_date:
                output.append(f"\n### Day Start: {dt.strftime('%B %d, %Y')}\n")
                last_date = current_date

            # Format with name and timestamp
            if full_meta:
                output.append(f"**{author_display}** [{current_time}]:\n")
            else:
                output.append(f"**{author_display}**:\n")
        else:
            output.append(f"**{author_display}**:\n")

        # Format message content
        formatted_content = format_message_content(content)
        output.append(formatted_content)

    return "\n".join(output)
