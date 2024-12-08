# Contributing to LemonSqueezy Py API

First off, thank you for considering contributing to LemonSqueezy Py API! 🎉

## Ways to Contribute

### 🐛 Report an Issue

The simplest way to contribute is to report an issue:

1. Check if the issue already exists in our [GitHub Issues](link-to-issues)
2. If not, create a new issue with:
   - A clear title
   - A detailed description
   - Steps to reproduce (if it's a bug)
   - Expected vs actual behavior
   - Your environment details (Python version, OS, etc.)

### 📖 Improve Documentation

Documentation improvements are always welcome! You can:

- Fix typos or clarify existing documentation
- Add missing documentation for existing features
- Write tutorials or usage examples
- Improve inline code comments

### 💻 Submit Code Changes

#### Development Setup

1. Fork and clone the repository
2. Set up your development environment:

```sh
# Create virtual environment using UV
uv venv

# Activate the environment
# On Windows:
.venv/Scripts/activate
# On Unix or MacOS:
source .venv/bin/activate

# Install dependencies
uv sync
```

#### Development Tools

This project uses several tools to maintain code quality:

##### Pre-Commit Hooks

We use pre-commit to ensure code quality. Set it up with:

```sh
# Install pre-commit hooks
uv run pre-commit install

# Run against all files
uv run pre-commit run -a
```

##### Testing

We use pytest for testing. You'll need a LemonSqueezy test store with API access to run the tests:

1. Create a test store in your [LemonSqueezy dashboard](https://app.lemonsqueezy.com/)
2. Generate an API key with appropriate permissions
3. Set up your environment variables:
   ```sh
   export LEMONSQUEEZY_API_KEY=your_test_api_key
   ```

Run tests with:

```sh
# Run all tests
uv run pytest

# Run specific test file
uv run pytest tests/test_specific.py

# Run with coverage
uv run pytest --cov=lemonsqueezy
```

Note: Never use a production API key for testing!

#### Pull Request Process

1. Create a new branch for your feature:

   ```sh
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and commit them:

   ```sh
   git commit -m "Description of your changes"
   ```

3. Ensure your code:

   - Passes all tests
   - Includes appropriate documentation
   - Follows the project's code style
   - Includes relevant tests for new features

4. Push your changes and create a Pull Request

### 🎨 Code Style

- Follow PEP 8 guidelines
- Use type hints
- Write descriptive docstrings
- Keep functions focused and concise
- Add comments for complex logic

## Questions?

Feel free to open an issue for any questions about contributing. We're here to help! 🚀
