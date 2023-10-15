from Fields import *


class Record:

    def add(self):
        pass

    def change(self):
        pass

    def delete(self):
        pass

    def find(self):
        pass

    def add_field(self, field, value):
        pass


class ContactRecord(Record):

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.address = None
        self.email = None
        self.birthday = None

    def add(self, field: Field, value: str):
        field.value(value)
        return 'Added phone value'
        
    def find(self, value: str):
        if value == 'phone':
            return self.phones
        elif value == 'name':
            return self.name
        elif value == 'address':
            return self.address
        elif value == 'email':
            return self.email
        elif value == 'birthday':
            return self.birthday
        else:
            return f'Not data'
        
    def add_phone(self, phone):
        self.phones.append(Phone(phone))
        
    def __str__(self):
        return f'Contact: {self.name};\nBirthday: {self.birthday};\nAddress: {self.address};\nEmail: {self.email};\nPhones:{self.phones})'
        

class NoteRecord(Record):

    pass