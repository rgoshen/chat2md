# 🗨️ chat2md

[![Build](https://github.com/rgoshen/chat2md/actions/workflows/python.yml/badge.svg)](https://github.com/rgoshen/chat2md/actions)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-0.1.0-blue.svg)](https://github.com/rgoshen/chat2md)

**chat2md** is a command-line tool that converts ChatGPT-style JSON exports into clean, timestamped, syntax-highlighted Markdown transcripts.

Whether you're documenting technical conversations, turning chats into blog posts, or archiving for future reference — `chat2md` has you covered.

## ✨ Features

- ✅ Converts ChatGPT JSON exports into well-structured Markdown
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

## 📦 Installation

### 1. Clone repository

```bash
git clone https://github.com/rgoshen/chat2md.git
cd chat2md
```

> **NOTE**:It is recommended to use a virtual environment for installation:

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install all dependencies

```bash
pip install -r requirements.txt
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

📝 Tip: You can also reinstall with the --editable . flag if you want live development changes reflected without reinstalling:

```bash
pipx install --editable . --force
```

### 🛠️ Install chat2md globally

If you don't want to or need to clone the repo then (still need pipx installed):

```bash
pipx install git+https://github.com/rgoshen/chat2md.git
```

Now you can run it from anywhere (see [Usage](#🧪-Usage)).

### 🔄 Update or Uninstall `chat2md` (pipx)

To update your installed version after making local changes:

```bash
pipx reinstall chat2md
```

If you need to uninstall:

```bash
pipx uninstall chat2md
```

## 🧪 Usage

```bash
chat2md path/to/chat.json output.md
```

- `chat.json` — ChatGPT-style export with messages
- `output.md` — Output Markdown file

### Example

```bash
chat2md tests/test_sample.json chat_transcript.md
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

Or, if you’ve installed the tool using pipx:

```bash
chat2md path/to/conversations.json
```

#### With optional flags

To include full metadata (YAML frontmatter, timestamps, and message IDs):

```bash
python3 chat2md.py path/to/conversations.json --full-meta
# or the short version:
python3 chat2md.py path/to/conversations.json -f
# or, if installed via pipx
chat2md.py path/to/conversations.json --full-meta
# or
python3 chat2md.py path/to/conversations.json -f
```

Each conversation will be exported to its own `.md` file in the current working directory.
File names are auto-generated from the conversation title and ID, for example:

```bash
My_Conversation_Title_a1b2c3d4.md
```

## 🧠 Supported JSON Format

The input must match ChatGPT’s export structure:

````json
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
````

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

chat2md/
├── chat2md/
│ ├── **init**.py
│ ├── chat2md_core.py
│ └── cli.py
├── tests/
│ ├── sample_conversations.json
| ├── test_full_meta.py
| └── test_standard_output.py
├── .github/workflows/
│ └── python.yml
├── setup.py
├── README.md
├── LICENSE
└── .gitignore

```

## 🧪 Development

### 🧪 Running Tests

#### 🧪 Run all tests

To run all tests:

```bash
pytest tests/
```

#### 🎯 Running a Specific Test

To run a specific test file:

```bash
pytest tests/test_standard_output.py
```

To run a specific test function:

```bash
pytest tests/test_standard_output.py::test_standard_markdown_output
```

You can also add `-v` for verbose output or `-x` to stop on the first failure:

```bash
pytest -v tests/test_standard_output.py::test_standard_markdown_output
```

### 🧼 Code Formatting

To automatically fix linting and formatting issues:

```bash
autopep8 chat2md/ --in-place --recursive --aggressive --aggressive
```

You can also run the linter manually:

```bash
flake8 chat2md
```

## 🚀 Roadmap

- [ ] Add automatic language inference from code snippets
- [ ] Support different output formats (HTML, PDF)
- [ ] Option to anonymize names or redact sensitive content
- [ ] Obsidian-flavored Markdown compatibility

## 🪪 License

[MIT](LICENSE)

## 👤 Author

**Rick Goshen**
💼 Software Engineer | 🧠 Lifelong Learner | 🛠 Builder of Tools

## 🙌 Contributions Welcome

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute.
