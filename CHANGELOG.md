# Changelog

## [] - 2025-05-03

### fix

- Pre-release from branch bugfix/fix-full-meta-data


## [] - 2025-05-03

### fix

- Pre-release from branch bugfix/fix-full-meta-data


## [] - 2025-05-03

### fix

- Pre-release from branch bugfix/fix-full-meta-data


## [] - 2025-05-03

### fix

- Pre-release from branch bugfix/fix-full-meta-data


## [] - 2025-05-03

### fix

- Pre-release from branch bugfix/fix-full-meta-data


All notable changes to this project will be documented in this file. See [standard-version](https://github.com/conventional-changelog/standard-version) for commit guidelines.

## 0.2.0 (2025-04-27)


### 🐛 Bug Fixes

* add filename for missing title ([136e96f](https://github.com/rgoshen/chat2md/commit/136e96f1781eeca2ccc6ed714fb01b2a50a36bba))

## [0.1.0] - 2025-04-16

### ✨ Added

- Initial CLI tool to convert ChatGPT JSON exports into timestamped Markdown.
- Support for full metadata export with `--full-meta` flag.
- Language detection for syntax-highlighted code blocks (`python`, `java`, `json`, `html`, etc.).
- Automatic date and time headers for conversations.
- One Markdown file generated per conversation with sanitized filenames.
- CLI interface using `argparse`.

### 🧱 Refactored

- Adopted clean architecture:
  - `adapters/` for file loading
  - `services/` for orchestration
  - `parsers/` for formatting logic
  - `utils/` for reusable tools (like `text_tools.py`)
- Separated single-conversation parsing from multi-conversation orchestration.
- Introduced `process_all_conversations()` to control core flow.

### 🧪 Testing

- Converted all test files to use `pytest` and centralized fixtures via `conftest.py`.
- Added fixture loader for `sample_conversations.json`.
- Verified full-meta output, filename sanitization, and adapter-level failures.

### 📚 Docs

- Fully updated `README.md` and `CONTRIBUTING.md`
- Added clean project layout and install instructions
- Clarified CLI behavior and pipx support
