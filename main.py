from collections import UserDict
from datetime import date

class Field:
    
    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self)->str:
        return self._value
    
    @value.setter
    def value(self, value: str)-> None:
        self._value = value

    def __str__(self):
        return str(self._value)


class Birthday(Field):

    # Реалізація класу
    @Field.value.setter
    def value(self, value: str)-> None:
        if value is None:
            self._value = ''
        else: 
            try:       
                day, month, year = value.split('.') 
                birthday_date = date(year=int(year), month=int(month), day=int(day))
                self._value = birthday_date
            except ValueError:
                raise ValueError('Date of birthday is not valid! (dd.mm.yyyy)')
            


class Name(Field):

    # Реалізація класу
    pass

class Phone(Field):

    # Реалізація класу
    @Field.value.setter
    def value(self, value: str)-> None:
        if len(value) == 10:
            self._value = value
        else: 
            raise ValueError('Phone number is not valid')

    
class Record:
    
    def __init__(self, name:str, phone:str=None, birthday:str=None):
        self.name = Name(name)
        self.phones = []

        if phone is not None:
            self.add_phone(phone)

        if birthday is not None:
            self.birthday = Birthday(birthday)
        else:
            self.birthday = Birthday(None)
        
    # Реалізація класу
    def add_phone(self, number: str)-> None:
        self.phones.append(Phone(number))

    def edit_phone(self, old_phone: str, new_phone: str)-> None:
        is_edited = False
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                is_edited = True

        # Якщо номера не існує, то викликається помилка  
        if not is_edited:
            raise ValueError(f'Phone number - {old_phone} is not exist in contact: {self.name}')    

    def find_phone(self, find_phone: str)-> Phone:
        for indx, phone in enumerate(self.phones):
            if phone.value == find_phone:
                return self.phones[indx]
            
    def remove_phone(self, remove_phone)-> None:
        for indx, phone in enumerate(self.phones):
            if phone.value == remove_phone:
                del self.phones[indx]

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def days_to_birthday(self):
        if self.birthday.value == '':
            return None
        today = date.today()
        actual_birthday = self.birthday.value.replace(year=today.year)
        if actual_birthday < today:
            actual_birthday = self.birthday.value.replace(year=today.year+1)
        time_to_birthday = abs(actual_birthday - today)

        return time_to_birthday.days
    
    def __str__(self):
        return f"| Contact name: {self.name.value:<10}| birthday: {str(self.birthday.value):<11}| phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):

    iter_records = 3

    # Реалізація класу
    def add_record(self, record: Record)-> None:
        self.data[record.name.value] = record

    def delete(self, name)-> None:
        if name in self.data:
            del self.data[name]

    def find(self, name: str)-> Record:
        if name in self.data:
            return self.data[name]
        
    def __iter__(self):
        self.idx = 0
        self.page = 0
        self.list_of_records = [record for record in self.data]

        return self

    def __next__(self):

        if self.idx >= len(self.data):
            raise StopIteration
        self.count_records = 1
        self.page += 1
        self.result = f'Page: {self.page}'

        while self.count_records <= self.iter_records:

            # Якщо на одному page буде не повна кількість викличеться IndexError
            # для цього повторно роблю перевірку і повертаю self.result
            if self.idx >= len(self.data):
                return self.result
            
            self.result += f'\n{self.data[self.list_of_records[self.idx]]}'
            self.count_records += 1
            self.idx += 1
                
        return self.result
    
    def set_iter_records(self, iter_records):
        self.iter_records = iter_records

        
    def __str__(self):

        if not self.data:
            return 'The phone dictionary is empty'
        else:
            self.result = 'The phone dictionary has next contacts:'
            for record in self.data:
                self.result += f'\n{str(self.data[record])}'
            self.result += '\n'

            return self.result


if __name__ == '__main__':

    print('----- Phone(Field)')
    phone = Phone('0123456789')
    print(phone.value)

    phone.value = '9876543210'
    print(phone.value)

    print('----- Birthday(Field)')
    birthday = Birthday('12.05.1990')
    print(birthday.value)

    birthday.value = '12.05.2023'
    print(birthday.value)

    print('----- Name(Field)')
    name = Name('Vitalii')
    get_name = name.value
    print(get_name)

    name.value = 'Bob'
    print(name.value)

    print('----- Record: add phone')
    bob_record = Record('Bob')
    bob_record.add_phone('0123456789')
    bob_record.add_phone('0001112233')
    print(bob_record)

    print('----- Record: edit phone')
    bob_record.edit_phone('0123456789', '0000000000')
    print(bob_record)
    # bob_record.edit_phone('1111111111', '0000000000')

    print('----- Record: add birthday')
    bob_record.add_birthday('30.09.1990')
    print(bob_record)

    print('----- Record: days_to_birthday')
    days = bob_record.days_to_birthday()
    print(days)

    print('----- AddressBook: Iter')
    # Створення нової адресної книги
    book = AddressBook()
    book.add_record(Record(name='Vitalii', phone='0000000000', birthday='12.05.1990'))
    book.add_record(Record(name='Tom', phone='1111111111', birthday='03.02.1977'))
    book.add_record(Record(name='Jane', phone='2222222222', birthday='06.01.1986'))
    book.add_record(Record(name='John', phone='3333333333'))
    book.add_record(Record(name='Andry', phone='4444444444', birthday='17.09.1980'))
    book.add_record(Record(name='Lisa', phone='5555555555', birthday='04.07.1975'))
    book.add_record(Record(name='Natasha', phone='6666666666', birthday='01.11.1991'))
    book.add_record(Record(name='Ira', phone='7777777777', birthday='09.10.1993'))
    book.add_record(Record(name='Vasya', phone='8888888888', birthday='09.05.1965'))
    book.add_record(Record(name='Ivan', phone='9999999999', birthday='21.04.1968'))
    book.add_record(Record(name='Stas', phone='0123456789', birthday='29.03.1974'))
    book.add_record(Record(name='Sasha', phone='9876543210'))
    book.add_record(Record(name='Marina', phone='1234567890', birthday='30.06.1976'))
    book.add_record(Record(name='Boston', phone='0987654321', birthday='10.09.1993'))
    book.add_record(Record(name='Vadim', phone='2345678901', birthday='12.10.1989'))
    book.add_record(Record(name='Oleg', phone='1098765432', birthday='13.01.1978'))
    book.add_record(Record(name='Valera', phone='3456789012', birthday='10.02.1974'))
    book.add_record(Record(name='Anya', phone='2109876543', birthday='15.08.1991'))
    book.add_record(Record(name='Kolya', phone='4567890123', birthday='16.03.1993'))
    book.add_record(Record(name='Misha', phone='3210987654', birthday='08.01.1990'))
    print(book)


    print('----- AddressBook: Iter')
    # Кількість записів на сторінці по замовчуванню
    for line in book:
        print(line)

    # Кількість записів на сторінці змінюємо на 5
    book.set_iter_records(5)

    print('\n----- AddressBook: Повторний Iter')
    for line in book:
        print(line)