import pickle
import json
import csv

from collections import UserDict
from datetime import date
from os import getcwd


# 1. Додати функціонал збереження адресної книги на диск та відновлення з диска.
#    - Для цього ви можете вибрати будь-який зручний для вас протокол 
#      серіалізації/десеріалізації даних та реалізувати методи, які дозволять 
#      зберегти всі дані у файл і завантажити їх із файлу
# 
# 2. Додати користувачеві можливість пошуку вмісту книги контактів.
#    - Щоб можна було знайти всю інформацію про одного або кількох користувачів 
#      за кількома цифрами номера телефону або літерами імені тощо.


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

    def add_birthday(self, birthday: str) -> None:
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
    
    def __str__(self) -> str:
        days = str(self.days_to_birthday())
        return f" Contact name: {self.name.value:<10} birthday: {str(self.birthday):<11}({days:<4} days) phones: {'; '.join(p.value for p in self.phones)}"
    
    def __repr__(self) -> str:
        self.phones_repr = ', '.join([phone.value for phone in self.phones])
        return f'Record({self.name.value}, {self.phones_repr}, {self.birthday.value})'


class AddressBook(UserDict):

    def __init__(self) -> None:
        super().__init__()
        self.file_name = 'address_book'
        self.iter_records = 3

        self.set_mode(mode='pickle')

    
    # Реалізація класу
    def add_record(self, record: Record)-> None:
        self.data[record.name.value] = record

    def delete(self, name)-> None:
        if name in self.data:
            del self.data[name]


    def _find_by_name(self, search_name: str) -> list:
        return filter(lambda key: search_name.lower() in key.lower(), self.data.keys())
    
    def _find_by_phone(self, search_phone: str) -> list:
        return filter(lambda record: True in [(search_phone in phone.value) for phone in self.data[record].phones], self.data)
    

    def find_record(self, search_data: str)-> str:
        """
        Дана функція шукає інформацію по користувачах, які мають 
        в імені або номері телефону є збіги із введеним рядком.
        """

        self.result = list()
        self.result.extend(self._find_by_name(search_data))
        self.result.extend(self._find_by_phone(search_data))
        # print('find', [str(self.data[record]) for record in self.result])
        
        if not self.result:
            return f'Not find contacts with search parameters "{search_data}"'
        else:
            self.str_result = f'The phone dictionary has next contacts with search parameters "{search_data}":'
            for ind, record in enumerate(self.result, start=1):
                # Якщо менше ind < 10, то буде 01, 02, ..., 09, якщо більше, то 10, 11, ...
                ind = f'0{ind}' if ind <= 9 else str(ind)
                self.str_result += f'\n{ind}. {str(self.data[record])}'
            self.str_result += '\n'

            return self.str_result

    def find(self, name:str) -> Record:
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

    def set_mode(self, mode: str) -> str:
        """
        You can change type of serialization
        - pickle    (default)
        - json      (don't work yet)
        - csv
        """
        if mode == 'pickle':
            self._file_full_name = self.file_name + '_pickle.bin'
            self.mode = 'pickle'
        elif mode == 'json':
            self._file_full_name = self.file_name + '_json.json'
            self.mode = 'json'
        elif mode == 'csv':
            self._file_full_name = self.file_name + '_csv.csv'
            self.mode = 'csv'
        else:
            raise ValueError('You entered wrong mode for export/import data')
        
        return f'Mode for export/import changed to: {self.mode}'
        
    def save(self):

        if self.mode == 'pickle':
            return self.save_data_to_pickle()
        elif self.mode == 'json':
            return self.save_data_to_json()
        elif self.mode == 'csv':
            return self.save_data_to_csv()

    def load(self):

        if self.mode == 'pickle':
            return self.load_data_from_pickle()
        elif self.mode == 'json':
            return self.load_data_from_json()
        elif self.mode == 'csv':
            return self.load_data_from_csv()

    def load_data_from_pickle(self) -> str:

        with open(self._file_full_name, 'rb') as fh:
            self.data = pickle.load(fh)
        
        return f'Address book was loaded from file:\n{getcwd()}\{self._file_full_name}'

    def save_data_to_pickle(self) -> str:

        with open(self._file_full_name, 'wb') as fh:
            pickle.dump(self.data, fh)
        
        return f'Address book was saved to file:\n{getcwd()}\{self._file_full_name}'
    
    def load_data_from_json(self):

        with open(self._file_full_name, 'r') as fh:
            self.data = json.load(fh)

        return f'Address book was loaded from file:\n{getcwd()}\{self._file_full_name}'

    def save_data_to_json(self) -> str:

        # Викликається помилка
        # raise TypeError(f'Object of type {o.__class__.__name__} '
        # TypeError: Object of type Record is not JSON serializable

        with open(self._file_full_name, 'w') as fh:
            json.dump(self.data, fh)

        return f'Address book was saved to file:\n{getcwd()}\{self._file_full_name}'

    def load_data_from_csv(self):
        import_data = dict()

        with open(self._file_full_name, 'r', newline='') as fh:
            csv_reader = csv.reader(fh)
            for row in csv_reader:
                name, birthday, *phones = row
                record = Record(name)
                if birthday != '':
                    year, month, day = birthday.split('-')
                    record.add_birthday(f'{day}.{month}.{year}')
                for phone in phones:
                    record.add_phone(phone)
                self.add_record(record)
        
        return f'Address book was loaded from file:\n{getcwd()}\{self._file_full_name}'

    def save_data_to_csv(self)-> str:

        export_data = dict()

        for name, record in self.data.items():
            export_data[name] = [str(record.birthday.value), *[phone.value for phone in record.phones]]
        
        with open(self._file_full_name, 'w', newline='') as fh:
            csv_writer = csv.writer(fh)
            for name, record in export_data.items():
                csv_writer.writerow([name, *record])
        
        return f'Address book was saved to file:\n{getcwd()}\{self._file_full_name}'

    def __str__(self):

        if not self.data:
            return 'The phone dictionary is empty'
        else:
            self.result = 'The phone dictionary has next contacts:'
            for ind, record in enumerate(self.data, start=1):
                ind = f'0{ind}' if ind <= 9 else str(ind)
                self.result += f'\n{ind}. {str(self.data[record])}'
            self.result += '\n'

            return self.result


if __name__ == '__main__':

    # print('----- Phone(Field)')
    # phone = Phone('0123456789')
    # print(phone.value)

    # phone.value = '9876543210'
    # print(phone.value)

    # print('----- Birthday(Field)')
    # birthday = Birthday('12.05.1990')
    # print(birthday.value)

    # birthday.value = '12.05.2023'
    # print(birthday.value)

    # print('----- Name(Field)')
    # name = Name('Vitalii')
    # get_name = name.value
    # print(get_name)

    # name.value = 'Bob'
    # print(name.value)

    # print('----- Record: add phone')
    # bob_record = Record('Bob')
    # bob_record.add_phone('0123456789')
    # bob_record.add_phone('0001112233')
    # print(bob_record)

    # print('----- Record: edit phone')
    # bob_record.edit_phone('0123456789', '0000000000')
    # print(bob_record)
    # # bob_record.edit_phone('1111111111', '0000000000')

    # print('----- Record: add birthday')
    # bob_record.add_birthday('30.09.1990')
    # print(bob_record)

    # print('----- Record: days_to_birthday')
    # days = bob_record.days_to_birthday()
    # print(days)

    # print('----- AddressBook: Iter')
    # Створення нової адресної книги
    # book = AddressBook()
    # book.add_record(Record(name='Vitalii', phone='0000000000', birthday='12.05.1990'))
    # book.add_record(Record(name='Vitalii', phone='0100000000'))
    # book.add_record(Record(name='Vitalii', phone='1100000000'))
                    
    # book.add_record(Record(name='Tom', phone='1111111111', birthday='03.02.1977'))
    # book.add_record(Record(name='Jane', phone='2222222222', birthday='06.01.1986'))
    # book.add_record(Record(name='John', phone='3333333333'))
    # book.add_record(Record(name='Andry', phone='4444444444', birthday='17.09.1980'))
    # book.add_record(Record(name='Lisa', phone='5555555555', birthday='04.07.1975'))
    # book.add_record(Record(name='Natasha', phone='6666666666', birthday='01.11.1991'))
    # book.add_record(Record(name='Ira', phone='7777777777', birthday='09.10.1993'))
    # book.add_record(Record(name='Vasya', phone='8888888888', birthday='09.05.1965'))
    # book.add_record(Record(name='Ivan', phone='9999999999', birthday='21.04.1968'))
    # book.add_record(Record(name='Stas', phone='0123456789', birthday='29.03.1974'))
    # book.add_record(Record(name='Sasha', phone='9876543210'))
    # book.add_record(Record(name='Marina', phone='1234567890', birthday='30.06.1976'))
    # book.add_record(Record(name='Boston', phone='0987654321', birthday='10.09.1993'))
    # book.add_record(Record(name='Vadim', phone='2345678901', birthday='12.10.1989'))
    # book.add_record(Record(name='Oleg', phone='1098765432', birthday='13.01.1978'))
    # book.add_record(Record(name='Valera', phone='3456789012', birthday='10.02.1974'))
    # book.add_record(Record(name='Anya', phone='2109876543', birthday='15.08.1991'))
    # book.add_record(Record(name='Kolya', phone='4567890123', birthday='16.03.1993'))
    # book.add_record(Record(name='Misha', phone='3210987654', birthday='08.01.1990'))
    # book.add_record(Record(name='vitalii', phone='0011223344', birthday='08.01.1991'))

    # print(book)


    # print('----- AddressBook: Iter')
    # # Кількість записів на сторінці по замовчуванню
    # for line in book:
    #     print(line)

    # # Кількість записів на сторінці змінюємо на 5
    # book.set_iter_records(5)

    # print('\n----- AddressBook: Повторний Iter')
    # for line in book:
    #     print(line)

    # print('\n----- AddressBook: Зберігання в pickle')
    # print(book.save_data_to_pickle())

    ...