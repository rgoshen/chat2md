# Contributing to chat2md

Thank you for considering contributing to **chat2md**! 🚀

Whether it's bug reports, new features, documentation, or just ideas — we welcome all types of contributions.

## 🧰 Getting Started

1. Fork the repository and clone your fork.
2. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install all dependencies

```bash
pip install -r requirements.txt
```

4. Create a new branch for your feature or bugfix.
5. Make your changes, and write tests if applicable.
6. Run the linter (`flake8`) to ensure style consistency.
7. Run all tests and verify they all pass.
8. Submit a pull request with a clear description.

## 🧪 Code Style

We use [PEP8](https://peps.python.org/pep-0008/) with `flake8`. Run it with:

```bash
flake8 chat2md
```

To automatically fix linting and formatting issues:

```bash
autopep8 chat2md/ --in-place --recursive --aggressive --aggressive
```

## 🧪 Running Tests

### 🧪 Run all tests

To run all tests:

```bash
pytest tests/
```

### 🎯 Running a Specific Test

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

## ✅ Checklist

Before submitting your contribution:

- [ ] My code follows the style guide
- [ ] I have performed a self-review of my code
- [ ] I have commented my code, especially in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] All tests pass

## 💬 Questions?

Open an issue or reach out to [@rgoshen](https://github.com/rgoshen).
