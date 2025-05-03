# 🗨️ chat2md

[![Tests](https://github.com/rgoshen/chat2md/actions/workflows/test.yml/badge.svg)](https://github.com/rgoshen/chat2md/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/rgoshen/chat2md/branch/main/graph/badge.svg)](https://codecov.io/gh/rgoshen/chat2md)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/rgoshen/chat2md?sort=semver)](https://github.com/rgoshen/chat2md/releases)
[![Python Versions](https://img.shields.io/pypi/pyversions/chat2md)](https://pypi.org/project/chat2md/)

**chat2md** is a command-line tool that converts ChatGPT-style JSON exports into clean, timestamped, syntax-highlighted Markdown transcripts.

Whether you're documenting technical conversations, turning chats into blog posts, or archiving for future reference — `chat2md` has you covered.

## ✨ Features

- ✅ Converts ChatGPT JSON exports into well-structured Markdown
- ✅ Shows progress bar during conversion
- ✅ Adds timestamped messages with human-readable formatting
- ✅ Supports optional YAML front matter with `--full-meta`
- ✅ Includes message IDs and model metadata (if available)
- ✅ Detects and syntax-highlights code blocks (`python`, `java`, `json`, `html`, `sql`, `javascript`)
- ✅ CLI interface for quick conversion
- ✅ GitHub Actions for linting and testing
- ✅ Linter (`flake8`) and formatter (`autopep8`) support for development
- ✅ Unit-tested using `pytest`, including standard and full-meta modes
- ✅ Easy to install locally or via `pipx`
- ✅ Extensible structure for future output formats (HTML, PDF, etc.)
- ✅ Support Python 3.13+

## 📦 Installation

### Requirements

- Python 3.13.3 or higher

### 1. Clone repository

```bash
git clone https://github.com/rgoshen/chat2md.git
cd chat2md
```

> **NOTE**:It is recommended to use a virtual environment for installation:

### 2. Run the setup script

```bash
# On macOS/Linux
./setup_chat2md.sh

# On Windows
setup_chat2md.bat
```

## 🚀 Optional: Install with `pipx` (Recommended for CLI Use)

[`pipx`](https://pypa.github.io/pipx/) is a tool that lets you run Python CLI apps in isolated environments — no need to activate virtual environments manually.

### 📦 Install `pipx` (if you haven't already)

```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

> ℹ️ You may need to restart your terminal after running ensurepath.

### 🛠️ Install chat2md globally from your local clone

```bash
cd chat2md
pipx install .
```

To reinstall with live-edit support:

```bash
pipx install --editable . --force
```

### Install chat2md directly from GitHub

```bash
pipx install git+https://github.com/rgoshen/chat2md.git
```

To update:

```bash
pipx reinstall chat2md
```

To uninstall:

```bash
pipx uninstall chat2md
```

## 🧪 Usage

```bash
chat2md path/to/chat.json
```

### ⚙️ Advanced CLI Options

You can include additional metadata in your Markdown output using the `--full-meta` flag.

### Options

| Flag                | Description                                                       |
| ------------------- | ----------------------------------------------------------------- |
| `-f`, `--full-meta` | Include rich metadata (YAML frontmatter, timestamps, message IDs) |

### Examples

#### Basic usage

```bash
python3 chat2md.py path/to/conversations.json
```

Or, if you've installed the tool using pipx:

```bash
chat2md path/to/conversations.json
```

#### With optional flags

To include full metadata (YAML frontmatter, timestamps, and message IDs):

| Flag                | Description                                                       |
| ------------------- | ----------------------------------------------------------------- |
| `-f`, `--full-meta` | Include rich metadata (YAML frontmatter, timestamps, message IDs) |

### Example

```bash
chat2md path/to/conversations.json -f
```

Each conversation will be exported to its own `.md` file in a `markdown_output` directory next to your input JSON file. For example, if your input file is `/path/to/conversations.json`, the output will be in `/path/to/markdown_output/`.

The tool shows a progress bar during conversion:

```bash
Converting conversations: 100%|██████████| 50/50 [00:05<00:00, 9.52 files/s]
```

File names are auto-generated from the conversation title and ID, for example:

```bash
My_Conversation_Title_a1b2c3d4.md
```

## 🧠 Supported JSON Format

The input must match ChatGPT's export structure:

```json
[
  {
    "title": "Sample Conversation",
    "id": "abc123",
    "create_time": 1712413000.0,
    "update_time": 1712413600.0,
    "mapping": {
      "msg1": {
        "message": {
          "id": "msg1",
          "author": { "role": "user" },
          "create_time": 1712413260.123,
          "content": { "parts": ["Hello, world!"] },
          "metadata": { "model_slug": "gpt-4" }
        }
      },
      "msg2": {
        "message": {
          "id": "msg2",
          "author": { "role": "assistant" },
          "create_time": 1712413290.456,
          "content": {
            "parts": [
              "Here's a Python snippet:\n```python\ndef hello(): pass\n```"
            ]
          },
          "metadata": {}
        }
      }
    }
  }
]
```

## 🖼️ Output Example

### Without full meta

````markdown
---

### Day Start: April 06, 2025

**Rick Goshen** [15:01:00]:
def add(a, b): return a + b

**ChatGPT** [15:01:30]:

```python
def add(a, b):
    return a + b
```

````

### Example Output with `--full-meta`

````markdown
---
title: 'Test Chat'
conversation_id: 'abc123'
created: '2024-12-01 12:34 UTC'
updated: '2024-12-01 14:21 UTC'
model: 'gpt-4'
---

### Day Start: April 06, 2025

**Rick Goshen** [15:01:00]:
def add(a, b): return a + b

**ChatGPT** [15:01:30]:

```python
def add(a, b):
    return a + b
```
````

## 📂 Project Structure

```bash
chat2md/                          # Root package
├── __init__.py
├── cli.py                        # CLI entry point
├── domain/                       # Domain layer
│   ├── __init__.py
│   ├── entities/                 # Core business objects
│   │   ├── __init__.py
│   │   └── conversation.py       # Conversation and Message entities
│   ├── exceptions.py            # Custom domain exceptions
│   └── repositories/            # Repository interfaces
│       ├── __init__.py
│       └── conversation_repository.py
├── application/                 # Application layer
│   ├── __init__.py
│   ├── interfaces/             # Application interfaces
│   │   ├── __init__.py
│   │   └── markdown_converter.py
│   └── use_cases/             # Business use cases
│       ├── __init__.py
│       └── convert_conversations.py
└── infrastructure/             # Infrastructure layer
    ├── __init__.py
    ├── config.py              # Configuration management
    ├── logging.py            # Logging setup
    ├── formatters/           # Output formatters
    │   ├── __init__.py
    │   └── markdown_formatter.py
    └── persistence/          # Storage implementations
        ├── __init__.py
        └── json_file_repository.py

tests/                        # Test suite
├── __init__.py
├── conftest.py              # Shared pytest fixtures
├── domain/                  # Domain layer tests
│   ├── __init__.py
│   └── test_exceptions.py
├── application/            # Application layer tests
│   ├── __init__.py
│   └── test_convert_conversations.py
└── infrastructure/        # Infrastructure layer tests
    ├── __init__.py
    ├── test_config.py
    └── test_logging.py

# Configuration files
├── .coveragerc             # Coverage configuration
├── codecov.yml            # Codecov settings
├── pytest.ini            # Pytest configuration
├── requirements.txt      # Project dependencies
└── setup.py             # Package setup
```

The project follows Clean Architecture principles:

- **Domain Layer**: Core business logic and entities
- **Application Layer**: Use cases and interfaces
- **Infrastructure Layer**: External concerns (I/O, formatting)

This separation ensures:

- Independence of business logic
- Easy testing and mocking
- Flexible implementation swapping
- Clear dependency direction (inward)

## 🧪 Development

chat2md is developed and tested with Python 3.13.3. Earlier versions may work but are not officially supported.

### Testing

Run all tests:

```bash
pytest
```

Run tests with coverage:

```bash
# Terminal report
pytest --cov=chat2md --cov-report=term-missing

# HTML report
pytest --cov=chat2md --cov-report=html

# XML report (for CI)
pytest --cov=chat2md --cov-report=xml
```

Coverage reports will be generated in:

- Terminal: Immediate output showing missing lines
- HTML: `coverage_html/` directory (open `index.html` in browser)
- XML: `coverage.xml` file (used by Codecov)

Current coverage requirements:

- Minimum coverage: 90%
- Branch coverage: Enabled
- Excluded from coverage:
  - `__repr__` methods
  - Type checking blocks
  - Main entry points
  - Import error handling

### Run specific test

```bash
pytest tests/test_standard_output.py
```

### Linting

```bash
flake8 chat2md
```

### Format (optional)

```bash
autopep8 chat2md/ --in-place --recursive --aggressive --aggressive
```

## 🚀 Roadmap

- [ ] Add automatic language inference from code snippets
- [ ] Support different output formats (HTML, PDF)
- [ ] Option to anonymize names or redact sensitive content
- [ ] Obsidian-flavored Markdown compatibility

## 📄 Changelog

See [CHANGELOG.md](CHANGELOG.md) for a full list of changes and version history.

## 🪪 License

[MIT](LICENSE)

## 👤 Author

**Rick Goshen**
💼 Software Engineer | 🧠 Lifelong Learner | 🛠 Builder of Tools

## 🙌 Contributions Welcome

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute.
