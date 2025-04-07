# 🗨️ chat2md

[![Build](https://github.com/rgoshen/chat2md/actions/workflows/python.yml/badge.svg)](https://github.com/rgoshen/chat2md/actions)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-0.1.0-blue.svg)](https://github.com/rgoshen/chat2md)

**chat2md** is a command-line tool that converts ChatGPT-style JSON exports into clean, timestamped, syntax-highlighted Markdown transcripts.

Whether you're documenting technical conversations, turning chats into blog posts, or archiving for future reference — `chat2md` has you covered.

## ✨ Features

- ✅ Converts ChatGPT JSON exports into well-structured Markdown
- ✅ Adds timestamped messages with human-readable formatting
- ✅ Groups messages by date with "Day Start" titles
- ✅ Detects and syntax-highlights code blocks (`python`, `java`, `json`, `html`, `sql`, `javascript`)
- ✅ CLI interface for quick conversion
- ✅ GitHub Actions for linting and testing
- ✅ Fully extensible and easy to customize

## 📦 Installation

It is recommended to use a virtual environment for installation:

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 1. Clone and install locally

```bash
git clone https://github.com/rgoshen/chat2md.git
cd chat2md
pip install .
```

> ✅ This makes `chat2md` available globally from your terminal.

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

## 🧠 Supported JSON Format

The input must match ChatGPT’s export structure:

````json
{
  "messages": [
    {
      "author": { "role": "user" },
      "create_time": 1712413260.123,
      "content": { "parts": ["Hello, world!"] }
    },
    {
      "author": { "role": "assistant" },
      "create_time": 1712413290.456,
      "content": {
        "parts": ["Here's a Python snippet:\n```python\ndef hello(): pass\n```"]
      }
    }
  ]
}
````

## 🖼️ Output Example

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

```

## 📂 Project Structure

```

chat2md/
├── chat2md/
│ ├── **init**.py
│ ├── chat2md_core.py
│ └── cli.py
├── tests/
│ └── test_sample.json
├── .github/workflows/
│ └── python.yml
├── setup.py
├── README.md
├── LICENSE
└── .gitignore

````

## 🧪 Development

Install the dev environment:

```bash
pip install -e .
pip install flake8
````

Run linter:

```bash
flake8 chat2md
```

Run test conversion:

```bash
chat2md tests/test_sample.json tests/output.md
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
