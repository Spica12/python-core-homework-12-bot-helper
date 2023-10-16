import pickle


class Storage:
    def save(self):
        pass

    def load(self):
        pass


class PickleStorage(Storage):

    def __init__(self, filename: str) -> str:
        self.filename = filename

    def save_object(self, object):
        with open(self.filename, 'wb') as fh:
            pickle.dump(object, fh)
    
    def load_object(self) -> object:
        with open(self.filename, 'rb') as fh:
            object = pickle.load(fh)
        return object
    

class Backup(Storage):

    def __init__(self, storage: Storage) -> None:
        self.storage = storage

    def save(self, object):
        return self.storage.save_object(object)

    def load(self):
        return self.storage.load_object()
    

# TODO Видалити коли буде не потрібно   
# Це тестовий if для перевірки працездатності коду. 
# if __name__ == "__main__":

#     class Test:
#         def __init__(self):
#             self.test = 10

#     storage_addressbook = Backup(PickleStorage('addressbook.bin'))
#     storage_notebook = Backup(PickleStorage('notebook.bin'))

#     object1 = Test()
#     object2 = Test()
#     object2.test = 20

#     print('----Value objects before saving')
#     print(object1.test)
#     print(object2.test)

#     storage_addressbook.save(object1)
#     storage_notebook.save(object2)

#     print('----Value objects after saving')
#     copy_object1 = storage_addressbook.load()
#     copy_object2 = storage_notebook.load()

#     print(copy_object1.test)
#     print(copy_object2.test)

