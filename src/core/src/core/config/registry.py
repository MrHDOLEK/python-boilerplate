_command_registry: list[type] = []


def command_group(name: str):
    def decorator(command_class):
        command_class._command_name = name
        _command_registry.append(command_class)
        return command_class

    return decorator


def get_registered_commands():
    return _command_registry
