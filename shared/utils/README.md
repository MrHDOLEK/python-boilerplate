# Shared Utils

Shared utilities and common functionality used across multiple modules in the project.

## Structure

```
shared/utils/
├── src/utils/        # Shared utilities source code
├── pyproject.toml    # Package configuration
└── README.md         # This file
```

## Overview

This package contains reusable utility functions, helpers, and common code that can be shared between different modules of the application. It provides a centralized location for:

- Common data structures and types
- Utility functions and helpers
- Shared configuration utilities
- Cross-module interfaces and contracts

## Installation

The shared utilities are installed as a local package dependency. To install in development mode:

```bash
pip install -e shared/utils/
```

## Usage

Import utilities from the shared package:

```python
from utils import your_utility_function
# or
from utils.module_name import specific_function
```

## Development

When adding new shared utilities:

1. Place them in the appropriate module under `src/utils/`
2. Update the package's `__init__.py` if needed
3. Add tests for new functionality
4. Update this README if adding major new features

## Dependencies

Check `pyproject.toml` for current dependencies and requirements.
