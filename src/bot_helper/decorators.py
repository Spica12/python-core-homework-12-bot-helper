
def input_error(func):
    """
    Всі помилки введення користувача повинні оброблятися за допомогою декоратора input_error. 
    Цей декоратор відповідає за повернення користувачеві повідомлень виду 
        "Enter user name", 
        "Give me name and phone please" і т.п. 
    Декоратор input_error повинен обробляти винятки, що виникають у функціях-handler 
    (KeyError, ValueError, IndexError) та повертати відповідну відповідь користувачеві.
    """

    def wrapper(*args, **kwargs):

        print(f'Wrapper in: func - {func.__name__}, args - {args}\n')
        
        try:
            return func(*args, **kwargs)

        except TypeError:
            return 'TypeError'
        
        # 'Give me name and phone please. Try again'

            # if func.__name__ == 'phone':
            #     return 'Enter user name. Try again'
            # else:
            #     return 'Give me name and phone please. Try again'
            
        except KeyError as e:
            print(e)
            return 'You entered a wrong command. Try again!'
        
    return wrapper
