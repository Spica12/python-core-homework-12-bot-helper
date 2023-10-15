from Books import Book, AddressBook, Notebook
from Fields import Field
from Records import Record, ContactRecord, NoteRecord
from Fields import Name


class Bot:

    

    def __init__(self, name):
        self.name = Name(name)
        self.addressbook = AddressBook()
        self.notebook = Notebook()
        

        self.COMMANDS_DICT = {
            'hello': self.say_hello,
            'close': self.say_goodbye,
            'help': self.help,
            # 'add': self.add,
            'show all': self.show_all_contacts,
            'add contact': self.add_contact,
            'delete contact': self.delete_contact,
            'add phone': self.add_phone
        }

    def parcer_input(self, user_input):
        new_input = user_input
        data = ''
        for key in self.COMMANDS_DICT:
            if user_input.strip().lower().startswith(key):
                new_input = key
                data = user_input[len(new_input):].split()
                break
        if data:
            return self.handler(new_input)(data)
        return self.handler(new_input)()
    
    def handler(self, reaction):
        return self.COMMANDS_DICT.get(reaction, self.break_func)
    
    def break_func():
        """
        Якщо користувач ввів якусь тарабарщину- повертаємо відповідну відповідь
        :return: Неправильна команда
        """
        return 'Wrong enter.'

    def help(self):
        message = 'I can do next commands:\n'
        for count, command in enumerate(self.COMMANDS_DICT):
            message = '\n'.join([message, f'{count}. {command}'])

        return message

    def say_hello(self):
        return f'Hello! I am {self.name.value}. How can I help you?'

    def say_goodbye(self):
        return 'Good Bye!'
    

    
    def add_contact(self, data):
    # def add_contact(self, name):
        name = data[0]
        record = ContactRecord(name)
        self.addressbook.add_record(record)

    def delete_contact(self, data):
        name = data[0]
        record: ContactRecord = self.addressbook.find(name)
        self.addressbook.delete_record(record)


    
    def add_phone(self, name, phone):
        record: ContactRecord = self.addressbook.find(name)
        record.add_phone(phone)

    

    def add(self, data):
        print(repr(data))
        type_field = data[0]
        name = data[1]
        print(type_field)

        if type_field == 'contact':
            record = ContactRecord(name)
            self.addressbook.add_record(record)
            return f'Contact was added'
        if type_field == 'note':
            record = NoteRecord(name)
            self.notebook.add_record(record)
            return f'Note was added'

        record = self.addressbook.find(type_field)
        if not record:
            record = self.notebook.find(type_field)
        if not record:
            return f'Record not found'
        
        field = record.find(type_field)
        record.add(*value)

    def show_all_contacts(self):
        return self.addressbook.show_all()


    

