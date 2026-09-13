IMAGE := "my-python-application:latest"
DOCKERFILE := ".docker/python/Dockerfile"

# Show all available recipes
default:
    @just --list

# Install all dependencies from the lockfile
sync:
    uv sync

# Install dependencies and register the pre-commit hooks
install: sync
    uv run pre-commit install

# Run the CLI, e.g. `just run user list`
run *ARGS:
    uv run core {{ ARGS }}

# Run the test suite, e.g. `just test -k users`
test *ARGS:
    uv run pytest {{ ARGS }}

# Run the test suite with a coverage report
test-cov:
    uv run pytest --cov=src

# Lint with ruff
lint:
    uv run ruff check .

# Lint with ruff and apply the safe fixes
lint-fix:
    uv run ruff check . --fix

# Format with ruff
fmt:
    uv run ruff format .

# Report formatting problems without rewriting files
fmt-check:
    uv run ruff format . --check

# Static type analysis with ty
typecheck:
    uv run ty check

# Security scan only (bandit rules, already part of `just lint`)
security:
    uv run ruff check . --select S

# Run every pre-commit hook against all files
hooks:
    uv run pre-commit run --all-files

# Full read-only quality gate: lint (incl. security), formatting, types, tests
check: lint fmt-check typecheck test

# Reformat and autofix, then run the full quality gate
fix: fmt lint-fix check

# Build the Docker image
docker-build:
    docker buildx build -f {{ DOCKERFILE }} -t {{ IMAGE }} .

# Run the CLI inside the Docker image, e.g. `just docker-run user list`
docker-run *ARGS:
    docker run -it --rm {{ IMAGE }} core {{ ARGS }}

# Refresh the lockfile without changing pinned versions
lock:
    uv lock

# Upgrade every dependency to the newest version the constraints allow
upgrade:
    uv lock --upgrade
    uv sync

# List dependencies that have a newer release available
outdated:
    uv tree --outdated --depth 1

# Bump the pre-commit hooks to their latest revisions
hooks-update:
    uv run pre-commit autoupdate

# Delete caches, build artifacts and coverage data
clean:
    rm -rf .cache .ruff_cache .mypy_cache .coverage htmlcov dist build
    find . -path ./.venv -prune -o -type d -name __pycache__ -exec rm -rf {} +
