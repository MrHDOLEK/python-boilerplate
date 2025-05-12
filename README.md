# Python boilerplate

<p align="center">
  <a href="https://github.com/astral-sh/uv" target="blank"><img src="https://github.com/astral-sh/uv/blob/8674968a17e5f2ee0dda01d17aaf609f162939ca/docs/assets/logo-letter.svg" height="60" alt="uv logo" /></a>
</p>

[![CodeQL](https://github.com/MrHDOLEK/python-boilerplate/actions/workflows/code-quality.yml/badge.svg?branch=main)](https://github.com/MrHDOLEK/python-boilerplate/actions/workflows/code-quality.yml)
[![GitHub CI](https://github.com/MrHDOLEK/python-boilerplate/actions/workflows/python.yml/badge.svg?branch=main)](https://github.com/MrHDOLEK/python-boilerplate/actions/workflows/python.yml)
[![GitHub license](https://img.shields.io/github/license/MrHDOLEK/python-boilerplate)](https://github.com/MrHDOLEK/python-boilerplate)
[![Python](https://img.shields.io/badge/python-3.13-blue.svg?logo=python&logoColor=white)](https://www.python.org/)

---
#### A Python boilerplate using modern dev tools

## Project setup

### Development environment

```bash
# Clone the repository
git clone https://github.com/MrHDOLEK/python-boilerplate.git

# Navigate to project directory
cd python-boilerplate/

# Checkout working branch
git checkout <branch>

# Setup Python environment
uv python install
uv venv
source .venv/bin/activate

# Install dependencies
uv sync

# Install pre-commit hooks
pre-commit install
```

## Tools & Features

### uv

Fast Python package manager, written in Rust. Configuration in `pyproject.toml` and dependencies locked in `uv.lock`.

```bash
# Install a package
uv pip install <package>

# Run a command in the environment
uv run pytest tests
```

### pre-commit

Framework for managing git hooks. Configuration in `.pre-commit-config.yaml`.

```bash
# Run against all files
pre-commit run --all-files
```

### ruff

Fast Python linter and formatter. Rules defined in `pyproject.toml`.

```bash
# Format code
uv run ruff format .

# Check code
uv run ruff check .
```

### Testing

Using pytest for tests:

```bash
# Run tests
uv run pytest tests

# Run tests with coverage
uv run pytest tests --cov=src
```

### Docker

```bash
# Login to GitHub Container Registry
echo $GITHUB_TOKEN | docker login ghcr.io -u $GITHUB_USERNAME --password-stdin
# Build production image
docker buildx build -f .docker/python/Dockerfile -t my-python-application:latest .
# Run the application
docker run -it --rm my-python-application:latest
```

## Documentation

Learn more at these links:

- [uv](https://github.com/astral-sh/uv)
- [pre-commit](https://pre-commit.com/)
- [ruff](https://github.com/astral-sh/ruff)
- [mypy](http://mypy-lang.org/)
- [bandit](https://bandit.readthedocs.io/)
- [pytest](https://docs.pytest.org/)
