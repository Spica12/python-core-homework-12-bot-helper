from collections import UserDict

from Records import *


class Book(UserDict):

    # def add_record(self, record: Record):
    #     self.data[record.name.value] =  record

    def add_record(self, name):
        pass

    def change_record(self, record: Record):
        pass

    # def delete(self, record: Record):
    #     pass

    def delete_record(self, record: Record):
        pass

    def find(self, name):
        for key in self.data:
            if key == name:
                return self.data[key]
            
    def show_all(self):
        message = 'Book has next records:\n'
        for count, key_record in enumerate(self.data, start=1):
            message = '\n'.join([message, f'{count}.\n{self.data[key_record]}'])

        return message



class AddressBook(Book):
    
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def delete_record(self, record: Record):
        del self.data[record.name.value]


class Notebook(Book):
    pass





