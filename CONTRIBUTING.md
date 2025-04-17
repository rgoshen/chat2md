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

3. Install the project with development dependencies:

```bash
pip install -e .[dev]
```

4. Create a new branch for your feature or bugfix:

```bash
git checkout -b feat/your-feature-name
```

5. Make your changes, and write/update tests if applicable.
6. Run the linter and formatter to ensure style consistency.
7. Run all tests and verify they pass.
8. Commit and push your changes:

```bash
git add .
git commit -m "feat: describe your change"
git push origin feat/your-feature-name
```

9. Submit a pull request with a clear description of your change.

## 🧪 Code Style

We follow [PEP8](https://peps.python.org/pep-0008/) and use:

```bash
flake8 chat2md
```

To auto-format (optional):

```bash
autopep8 chat2md/ --in-place --recursive --aggressive --aggressive
```

## 🧪 Running Tests

Run all tests:

```bash
pytest
```

Run a specific test file:

```bash
pytest tests/test_standard_output.py
```

Run a specific test function with verbose output:

```bash
pytest -v tests/test_standard_output.py::test_standard_markdown_output
```

Stop on first failure:

```bash
pytest -x
```

## ✅ Contribution Checklist

- [ ] Code follows style guidelines
- [ ] All existing and new tests pass
- [ ] Tests are added or updated for new logic
- [ ] Code is well-commented and clear
- [ ] Pull request describes the change and links to any issues (if applicable)

## 🙋 Questions?

Feel free to open an issue or reach out to [@rgoshen](https://github.com/rgoshen).

Thanks for helping make `chat2md` awesome! 🙌
