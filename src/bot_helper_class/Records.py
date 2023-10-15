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

            
    def add_phone(self, phone):
        self.phones.append(Phone(phone))
        
    def __str__(self):
        phones = '; '.join([phone.value for phone in self.phones])
        return f'Contact: {self.name};\nBirthday: {self.birthday};\nAddress: {self.address};\nEmail: {self.email};\nPhones:{phones}'
        

class NoteRecord(Record):

    pass