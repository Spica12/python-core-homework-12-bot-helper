"""
В даному модулі описуються всі команди які може виконувати бот
"""

from decorators import input_error
from address_book_classes import book, Record


@input_error
def add(name, phone_number):
    """
    "add ..."
    За цією командою бот зберігає у пам'яті (у словнику наприклад) новий контакт. 
    Замість ... користувач вводить ім'я та номер телефону, обов'язково через пробіл.
    """
    record = book.find(name)
    if record is None:
        book.add_record(Record(name=name, phone=phone_number))
        return book.find(name)
    else:
        record.add_phone(phone_number)
        return record


def goodbye():
    """
    "good bye", 
    "close", 
    "exit" 
    По будь-якій з цих команд бот завершує свою роботу після того, як виведе у консоль "Good bye!".
    """
    return 'Good Bye!'


def hello():
    """
    "hello"
    Відповідає у консоль "How can I help you?"
    """
    return '\nHow can I help you?'


def return_wrong_command() -> str:
    """
    В разі якщо користувач ввів не правильну команду, то повертається 
    повідомлення про неправильний ввід
    """
    return 'You entered a wrong command. Try again!'
