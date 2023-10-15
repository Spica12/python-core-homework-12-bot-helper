
from datetime import datetime
from collections import UserDict


class Field:

    def __init__(self, value: str) -> None:
        self._value = None
        self.value = value

    @property
    def value(self) -> str:
        return self._value
    

class Name(Field):

    # Реалізація класу
    ...


class Phone(Field):

    # Реалізація класу
    @Field.value.setter
    def value(self, value: str) -> None | str:
        if not len(value) == 10:
            raise ValueError("Phone must contains 10 symbols.")
        if not value.isnumeric():
            raise ValueError("Phone number is not valid.")
        self._value = value


class Birthday(Field):

    # Реалізація класу
    @Field.value.setter
    def value(self, value: str) -> None | str:
        today = datetime.now().date()
        birthday = datetime.strptime(value, '%Y-%m-%d').date()
        if birthday > today:
            raise ValueError('Birthday must be less than current year and date.')
        self._value = value


class Record:

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone: str) -> None:
        self.phones.append(Phone(phone))

    # def __str__(self) -> str:
    #     days = str(self.days_to_birthday())
    #     return f" Contact name: {self.name.value:<10} birthday: {str(self.birthday):<11}({days:<4} days) phones: {'; '.join(p.value for p in self.phones)}"

    # def __repr__(self) -> str:
    #     self.phones_repr = ', '.join([phone.value for phone in self.phones])
    #     return f'Record({self.name.value}, {self.phones_repr}, {self.birthday.value})'


class AddressBook(UserDict):

    def __init__(self):
        super().__init__()

        # self.load_contacts_from_file()

    def add_record(self, record: Record)-> None:
        self.data[record.name.value] = record

    def find(self, name: str) -> Record | None:
        if name in self.data:
            return self.data[name]

    





book = AddressBook()
