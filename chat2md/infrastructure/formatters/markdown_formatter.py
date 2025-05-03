from chat2md.application.interfaces.markdown_converter import MarkdownConverter
from chat2md.domain.entities.conversation import Conversation
from chat2md.utils.text_tools import detect_language, is_probably_code


class DefaultMarkdownFormatter(MarkdownConverter):
    """Default implementation of the markdown converter using the existing text tools."""

    def convert_to_markdown(
        self,
        conversation: Conversation,
        include_metadata: bool = False
    ) -> str:
        output = []
        last_date = None

        # Add YAML frontmatter if metadata is requested
        if include_metadata:
            frontmatter = [
                "---",
                f"title: '{conversation.title}'",
                f"conversation_id: '{conversation.id or ''}'",
                f"created: '{conversation.create_time or ''}'",
                f"updated: '{conversation.update_time or ''}'",
                f"model: '{conversation.model or ''}'",
                "---",
                "",
                ""  # Extra newline after frontmatter
            ]
            output.extend(frontmatter)

        # Process each message
        for message in conversation.messages:
            if not message.content.strip():
                continue

            # Handle date headers and timestamps
            if message.create_time and include_metadata:
                current_date = message.create_time.strftime("%Y-%m-%d")
                current_time = message.create_time.strftime("%H:%M")

                if last_date != current_date:
                    if last_date is not None:
                        output.append("")  # Add blank line before new date section
                    output.append(f"## {current_date}")
                    output.append("")  # Add blank line after date header
                    last_date = current_date

                # Include timestamp and message ID with author
                output.append(
                    f"**[{current_time}] {message.author.capitalize()}:** "
                    f"(id: `{message.message_id or ''}`):"
                )
            else:
                # Only include author when not in full metadata mode
                output.append(f"**{message.author.capitalize()}:**")

            # Format content, detecting and handling code blocks
            content = message.content.strip()
            if is_probably_code(content):
                language = detect_language(content)
                output.append(f"```{language}")
                output.append(content)
                output.append("```")
            else:
                output.append(content)

            output.append("")  # Add blank line after each message

        # Ensure there's a trailing newline at the end of the file
        if not output[-1] == "":
            output.append("")

        return "\n".join(output)
