import os

from main_old import AddressBook, Record, Phone, Birthday, Name, Phone


"""
<project>
├── src
│   ├── <module>/*
│   │    ├── __init__.py
│   │    └── many_files.py
│   │
│   └── tests/*
│        └── many_tests.py
│
├─   .gitignore
├── pyproject.toml
└── README.md
"""


class Bot():

    def __init__(self, name: str) -> None:
        self.name = Name(name)
        self.window = MainWindow()
        self.window.bot_name = self.name

    def input_error(func):

        def wrapper(*args, **kwargs):
            if DEBUG:
                print(f'Wrapper: func - {func.__name__}, args - {args}\n')
            try:
                return func(*args, **kwargs)

            except TypeError:
                return 'Give me name and phone please. Try again'
            except KeyError:
                return 'You entered a wrong command. Try again!'

        return wrapper

    def greeting(self) -> str:

        return f'Hello! How can I help you?'
    
    @input_error
    def parse_input(self):

        ...
    
    def user_input(self) -> str:
        self.user = input('>>> ')
    

class MainWindow():
    
    def __init__(self) -> None:
        self.width = 71
        self.high = 5
        self.hor_border = '-'
        self.ver_border = '|'

        self.book = ''
        self.path = ''
        self.data = None
        self.bot_name = ''
        self.bot_msg = ''



    """
    BOT HELPER. Modul 12
    -----------------------------------------------------------------------
    | AddressBook:                                                        |
    | Path:                                                               |
    -----------------------------------------------------------------------
    |                                                                     |
    |                                                                     |
    |                                                                     |
    |                                                                     |
    |                                                                     |
    -----------------------------------------------------------------------
 Bob:  Hello! How can I help you?
    
    """
    def field(self, left, title, data, right):
        len_title = len(title) + 5
        return f'{left} {title} {data:<{self.width - len_title}} {right}\n'
    
    def horizontal_line(self, border: str, width: int)-> str:
        return f'{border * width}\n'


    def show(self) -> None:
         # Оновлення екрану 
        os.system('cls')
        
        output = ''
        # Title
        output += self.field(left='', title=NAME, data='', right='')
        # AddressBoor
        output += self.horizontal_line(self.hor_border, self.width)
        output += self.field(left=self.ver_border, title='AddressBook: ', data=self.book, right=self.ver_border)
        output += self.field(left=self.ver_border, title='Path: ', data=self.path, right=self.ver_border)

        output += self.horizontal_line(self.hor_border, self.width)
        # Data
        if self.data is None:
            for row in range(self.high):
                output += self.field(left=self.ver_border, title='', data='', right=self.ver_border)
        else:
            for row in self.data:
                output += self.field(left=self.ver_border, title='', data=self.data, right=self.ver_border)

        output += self.horizontal_line(self.hor_border, self.width)
        # Bot
        output += self.field(left='', title=f'{self.bot_name}: ', data=self.bot_msg, right='')

        print(output)

        





def main():

    bot = Bot('Bob')
    window = MainWindow()

    window.bot_name = bot.name
    window.bot_msg = bot.greeting()
    window.show()


    while True:

        bot.user_input()
        bot.parse_input()

       

        window.show()





if __name__ == '__main__':

    DEBUG = True
    NAME = 'BOT HELPER. Modul 12'
    
    main()
