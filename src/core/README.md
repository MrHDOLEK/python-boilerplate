# Core Module

Core application module providing CLI interface and business logic functionality.

## 📁 Structure

```
src/
├── clients/          # HTTP clients and external integrations
├── commands/         # CLI command implementations
├── config/           # Configuration management
│   ├── config.yaml   # Application configuration
│   └── logger_config.py
├── exceptions/       # Custom exception classes
├── models/           # Data models and schemas
│   └── config.py     # Settings and configuration models
├── services/         # Business logic services
├── utils/            # Core utilities
└── main.py           # Application entry point
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
