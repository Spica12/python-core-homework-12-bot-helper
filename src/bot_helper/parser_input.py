from handler import COMMANDS


def parse_input(user_input: str) -> str:
    """
    Даний модуль приймає на вхід інформацію від користувача, та повертає
    команду та додаткову інформацію до цієї команди
    """
    command: str = ''
    data: list = None

    for key in COMMANDS:
        if user_input.lower().startswith(key):
            command = key
            data = user_input[len(command):].split()
            break
        
    return command, data