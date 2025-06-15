_command_registry = []


def command_group(name: str):
    def decorator(cls):
        cls._command_name = name
        _command_registry.append(cls)
        return cls

    return decorator


def get_registered_commands():
    return _command_registry
