# Contributing to chat2md

We love your input! We want to make contributing to chat2md as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

## Development Process

We use GitHub to host code, to track issues and feature requests, as well as accept pull requests.

1. Fork the repo and create your branch from `main`
2. If you've added code that should be tested, add tests
3. If you've changed APIs, update the documentation
4. Ensure the test suite passes
5. Make sure your code meets our coverage requirements
6. Issue that pull request!

## Code Quality Requirements

### Test Coverage

We maintain high code quality through comprehensive testing:

- Minimum coverage requirement: 90%
- Branch coverage is enabled and required
- All new code must include tests
- Run tests with coverage: `pytest --cov=chat2md`

### What's Not Counted in Coverage

The following are excluded from coverage requirements:

- `__repr__` methods
- Type checking blocks
- Main entry points
- Import error handling
- Debug-only code

### Code Style

- We use `flake8` for linting
- Format code with `autopep8`
- Follow PEP 8 guidelines
- Use type hints where possible

## Pull Request Process

1. Update the README.md with details of changes to the interface
2. Update the CHANGELOG.md with a note describing your changes
3. The PR will be merged once you have the sign-off of at least one maintainer
4. All tests must pass and coverage requirements must be met

## Any contributions you make will be under the MIT Software License

In short, when you submit code changes, your submissions are understood to be under the same [MIT License](LICENSE) that covers the project. Feel free to contact the maintainers if that's a concern.

## Report bugs using GitHub's [issue tracker](https://github.com/rgoshen/chat2md/issues)

We use GitHub issues to track public bugs. Report a bug by [opening a new issue](https://github.com/rgoshen/chat2md/issues/new/choose).

## Write bug reports with detail, background, and sample code

**Great Bug Reports** tend to have:

- A quick summary and/or background
- Steps to reproduce
  - Be specific!
  - Give sample code if you can
- What you expected would happen
- What actually happens
- Notes (possibly including why you think this might be happening, or stuff you tried that didn't work)

## License

By contributing, you agree that your contributions will be licensed under its MIT License.
