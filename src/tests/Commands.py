

def add():
    """
    add phone <name> <phone>
    add birthday <name> <date>
    add address <name> <address>
    add email <name> <email>
    add note <note>
    add tag <note> <tag>
    
    Функція повертає:
    - Повідомлення, що <об'єкт> було добавлено в <місце>
    - повідомлення про помилку
    """
    pass


def change():
    """
    change phone <name> <phone>
    change birthday <name> <date>
    change address <name> <address>
    change email <name> <email>
    change note <note>
    change tag <note> <tag>

    Функція повертає:
    - Повідомлення, що <об'єкт> було змінено з <old_value> на <new_value>
    - повідомлення про помилку
"""
    pass


def delete():
    """
    delete phone <name> <phone>
    delete birthday <name> <date>
    delete address <name> <address>
    delete email <name> <email>
    delete record <name>
    delete note <note>
    delete tag <note> <tag>
    
    Функція повертає:
    -Повідомлення, що <об'єкт> було з <місце>
    -повідомлення про помилку
    """
    pass


def find():
    """
    find record <name (можна частково)>
    find record <phone (можна частково)>
    find record <birthday (можна частково)>
    find record <address (можна частково)>
    find record <email (можна частково)>
    find note <що знайти>
    find tag <tag (можна частково)>
    
    Функція повертає:
    - Записи, що відповідають критеріям пошуку.
    - Нотатки, що відповідають критеріям пошуку.
    - Повідомлення, що по таким критеріям нічого не знайдено.
    - повідомлення про помилку
    """
    pass


def get_help():
    """
    help

    Функція повертає:
    -   
    """
    pass


def get_next_birthday():
    """
    birthday <name (можна частково)>
    
    Функція повертає:
    - Кількість днів до наступного дня народження, якщо в записі вказано день народження.
    - Повідомлення, що для такого запису еднь народження не задано
    - Повідомлення, що такого запису <name> не існує.
    
    Якщо реалізовувати частковий пошук, то мабуть треба щоб виводило перелік записів, що відповідають критерію.
    """
    pass


def goodbye():
    """
    good bye 
    close 
    exit 

    Функція повертає:
    - По будь-якій з цих команд бот завершує свою роботу після того, як виведе у консоль "Good bye!".
    """
    pass


def hello():
    """
    hello

    Функція виконує:
    - None

    Функція повертає:
    - Відповідає у консоль "How can I help you?"
    """
    pass


def sort_dir():
    """
    sort <path dir>

    Функція виконує:
    - Сортує <path dir>

    Функція повертає:
    - Повідомлення про те що <path dir> відсортовано
    - Повідомлення, що такої папки не існує
    """
    pass


def show_all():
    """
    Користувач вводить наступні команди через пробіл:
    show all
    
    Функція повертає:   
    - всі збереженні контакти з номерами телефонів у консоль.
    """
    pass
