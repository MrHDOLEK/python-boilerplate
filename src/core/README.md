# Core Module

Core application module providing CLI interface and business logic functionality.

## 📁 Structure

```
   src/
   ├── core/                 # Core module source code
   │   ├── clients/          # HTTP clients and external integrations
   │   ├── commands/         # CLI command implementations
   │   ├── config/           # Configuration management
   │   ├── core/             # Core functionality
   │   ├── exceptions/       # Custom exception classes
   │   ├── models/           # Data models and schemas
   │   ├── services/         # Business logic services
   │   ├── utils/            # Core utilities
   │   └── main.py           # Application entry point
   └── tests/        # Core module tests
```

## 🚀 Usage

### Run the application

```bash
uv run core
```

### Show help and available commands

```bash
uv run core --help
```

### Get help for specific command

```bash
uv run core [command] --help
```

## 📋 Available Commands

To see all available commands, run:

```bash
uv run core --help
```
