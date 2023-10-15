from datetime import datetime


class Field:
    def __init__(self, value):
        self._value = value
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = self.validate(self.normalize(value))

    def normalize(self, value: str) -> str:
        return value
    
    def validate(self, value: str) -> str:
        return value

    def __str__(self):
        return f'{self._value}'


class Name(Field):

    def normalize(self, name: str) -> str:
        return name.title()


class Phone(Field):

    def normalize(self, value: str) -> str:
        new_value = (
            value.removeprefix("+")
                .replace("(", "")
                .replace(")", "")
                .replace("-", "")
                .replace(" ", "")
        )
        return new_value
    
    def validate(self, value: str) -> str:
        if len(value) < 10 or len(value) > 12:
                return f"Phone '{value}' must contains 10 symbols."
        if not value.isnumeric():
                return 'Wrong phones.'
        return value


class Birthday(Field):

    def normalize(self, birthday: str) -> str:
        normal_birthday = datetime.strptime(birthday, '%Y-%m-%d').date()                    # TODO Якщо дата не в правильному форматі викличеться ValueError. Її треба якось обробити
        return normal_birthday

    def validate(self, birthday: str) -> str:
        today = datetime.now().date()
        if birthday > today:
            return f"Birthday '{birthday}' must be less than current year and date."
        return birthday


class Address(Field):
    pass


class Email(Field):
    pass


if __name__ == '__main__':
    field_name = Name('vitalii savenko')
    print(field_name)

    field_phone = Phone('+38(063)-760-96-40')
    print(field_phone)

    field_birthday = Birthday('1990-05-12')
    print(field_birthday)
