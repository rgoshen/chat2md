from chat2md.utils.filename_tools import sanitize_filename

def test_removes_common_unsafe_characters():
    unsafe = 'CI/CD: with GitHub!?'
    assert sanitize_filename(unsafe) == 'CICD_with_GitHub'

def test_replaces_spaces_with_underscores():
    title = "A very long conversation"
    assert sanitize_filename(title) == "A_very_long_conversation"

def test_preserves_safe_titles():
    title = "Valid_Conversation_123"
    assert sanitize_filename(title) == title

def test_handles_mixed_safe_and_unsafe():
    title = "Hello: World/Test! Here?"
    assert sanitize_filename(title) == "Hello_WorldTest_Here"

def test_empty_string_returns_empty():
    assert sanitize_filename("") == ""

def test_only_unsafe_characters_returns_empty():
    assert sanitize_filename("/\\:*?\"<>|") == ""
