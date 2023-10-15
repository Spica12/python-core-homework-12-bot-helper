import commands


def handler(command: str) -> object:
    """
    Приймає команду та повертає функцію, що повинен виконати бот
    """
    print(f'handler: {command = }')

    return COMMANDS[command]


# Перелік команд які може виконувати бот

COMMANDS = {
    'hello': commands.hello,
    'add': commands.add,
    'change': None,
    'phone': None,
    'show all': None,
    'good bye': commands.goodbye,
    'close': commands.goodbye,
    'exit': commands.goodbye,
    '': commands.return_wrong_command,
}