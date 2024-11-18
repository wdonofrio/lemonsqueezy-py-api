# Contributing

Thanks for taking the time to contribute!

## How to Contribute

### Report an Issue

Simplest way to contribute is to report an Issue.
If you encounter a bug or have a feature request, let us know!

### Documentation

Improving documentation is a great way to learn more and help others.

-- Under Construction --

### Code

#### UV

This project uses [UV](https://docs.astral.sh/uv/). Ensure UV is installed before continuing.

1. Create venv with `uv venv`
2. Sync project with `uv sync`

### Testing

Run tests often to verify changes have not had unexpected side-effects.

#### Pre-Commit

This project uses pre-commit.  
Run `uv run pre-commit install` so that pre-commit is executed on commit.

Alternatively, `uv run pre-commit run -a` will test the codebase.

#### Pytest

This project uses pytest for unit-testing.  
Run `uv run pytest` to execute all tests.
