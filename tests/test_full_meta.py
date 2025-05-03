from chat2md.services.conversation_service import process_all_conversations


def test_full_meta_output(tmp_path, sample_conversation_dict):
    # Run full-meta markdown export using in-memory fixture
    process_all_conversations(sample_conversation_dict, output_dir=tmp_path, full_meta=True)

    md_files = list(tmp_path.glob("*.md"))
    assert md_files

    content = md_files[0].read_text(encoding="utf-8")
    # Verify YAML frontmatter is present and includes the expected metadata keys
    # The markdown file should begin with '---', followed by the frontmatter and a closing '---'
    assert content.startswith("---"), "Markdown file does not start with YAML frontmatter"
    parts = content.split("---")
    assert len(parts) >= 3, "YAML frontmatter not properly delimited by '---'"
    yaml_frontmatter = parts[1]
    for key in ("title", "conversation_id", "created", "updated", "model"):
        assert key in yaml_frontmatter, f"Missing required key '{key}' in YAML frontmatter"

    # Check date headers
    assert any(line.startswith("## ") for line in content.splitlines())
    # Check timestamps
    assert any("[" in line and "]" in line for line in content.splitlines())
    # Check that IDs are present in full meta mode
    assert "(id: `" in content
