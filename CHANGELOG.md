# Changelog

## [0.2.1](https://github.com/rgoshen/chat2md/compare/v0.2.0...v0.2.1) (2025-05-03)


### ✨ Features

* add create lables permission ([0f78b6b](https://github.com/rgoshen/chat2md/commit/0f78b6bad3addd16e9801d7aa711c7bd85497bb1))
* add versioning ([af3cf73](https://github.com/rgoshen/chat2md/commit/af3cf736f546c3906bc3019f65b06e8a61ba52e8))


### 🐛 Bug Fixes

* ensure newline at end of file in __init__.py ([6f8e3d9](https://github.com/rgoshen/chat2md/commit/6f8e3d99520d771bfac1d379edf6c922b51e7035))
* **release:** 0.2.0-bugfix-fix-full-meta-data.20250503010355 [skip ci] ([47f08f8](https://github.com/rgoshen/chat2md/commit/47f08f872e4273e15ae2403404264e5de2be4d4f))
* **release:** 0.2.0-bugfix-fix-full-meta-data.20250503010751 [skip ci] ([8dace0d](https://github.com/rgoshen/chat2md/commit/8dace0d97b81d2437730908515197891321030e9))
* **release:** 0.2.0-bugfix-fix-full-meta-data.20250503011546 [skip ci] ([39e8b69](https://github.com/rgoshen/chat2md/commit/39e8b696dca2802a115aeb47929c934a6edba17d))
* **release:** 0.2.0-bugfix-fix-full-meta-data.20250503012216 [skip ci] ([2e0039a](https://github.com/rgoshen/chat2md/commit/2e0039a8d2ef51b6eae2fcdb90ae91b3dd64ab11))
* **release:** 0.2.0-bugfix-fix-full-meta-data.20250503012647 [skip ci] ([7f417a5](https://github.com/rgoshen/chat2md/commit/7f417a579003b98b919ce0f7477bce8b2c4bd687))


### 🧱 Maintenance

* add release-please manifest file ([b5f8b7a](https://github.com/rgoshen/chat2md/commit/b5f8b7a7b910cbff9293fe2334aa215858127d09))
* remove local path for chat2md in requirements.txt ([79c2499](https://github.com/rgoshen/chat2md/commit/79c249929f78c3ec05083a8dc141c5b568c65b27))


### 🧪 Refactoring

* replace versioning configuration and workflows for branch releases ([1634141](https://github.com/rgoshen/chat2md/commit/163414147f43bb5a701ac29005696d802b725e62))


### 👨‍💻 Testing

* add validation for YAML frontmatter in markdown output ([495b1e4](https://github.com/rgoshen/chat2md/commit/495b1e4a083863246f99697f84982a59ab1a7701))

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
