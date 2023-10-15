from parser_input import parse_input
from handler import handler


def main():
    '''
    Основна логіка бота. 
    Отримання команди від користувача, обробка, вивід результату.
    '''
    while True:
        # Запит у користувача
        user_input = input('>>> ')

        # Обробка запиту
        command, data = parse_input(user_input)
        print(f'main: {command = }, {data = }')

        # Виклик необхідної команди згідно запиту
        if command != '' and data:
            result = handler(command)(data)
        else:
            result = handler(command)()

        print(result)
        if result == 'Good Bye!':
            break


if __name__ == '__main__':
    main()