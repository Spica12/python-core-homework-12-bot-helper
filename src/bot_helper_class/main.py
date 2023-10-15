import os

from Bot import Bot


def main():
    """
    Основна логика усього застосунку. Отримуємо ввід від користувача
    і відправляємо його в середину застосунку на обробку.
    :return:
    """
    bot = Bot('Bob_bot')
    bot.say_hello()

    try:
        while True:
            """
            Просимо користувача ввести команду для нашого бота
            Також тут же вимикаємо бота якщо було введено відповідну команду
            """

            user_input = input('>>> ')
            os.system('cls')
            result = bot.parcer_input(user_input)
            print(result)
            if result == 'Good Bye!':
                break
    finally:
        # contacts_dict.save_contacts_to_file()
        pass


if __name__ == '__main__':
    main()