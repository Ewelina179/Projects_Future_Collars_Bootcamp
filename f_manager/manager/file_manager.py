import os
import json, pickle

class File_Manager:
    ALLOWED_EXTENSIONS = (
        'json',
        'csv',
        'pickle'
    )

    def __init__(self, file, file_to_write, path="", *args):
        self.file = file
        self.path = path
        self.filetype = self.set_filetype(self.file)
        self.is_path_exist = self.validate_path()
        self.mode_from_read = self.set_mode_from_read()
        self.to_read = open(self.get_filepath(), self.mode_from_read)
        self.file_to_write = file_to_write
        self.filetype_to_write = self.set_filetype(self.file_to_write)
        self.to_change = args
        self.validated = self.validate()
        self.data = self.set_data()
        self.changes = self.lst_of_changes()
        self.mode_to_write = self.set_mode_to_write()
        self.to_write = open(self.file_to_write, self.mode_to_write)
        self.changed_file = self.change_file()
        self.changed = self.save_file_to()

    def validate(self):
        if self.filetype not in self.ALLOWED_EXTENSIONS:
            print("Nieobslugiwany format")
            return False
        return True

    def validate_path(self):
        if not os.path.exists(self.file):
            raise FileNotFoundError(f"Lista plików w podanej lokalizacji: {os.listdir(os.curdir)}")
            
    def lst_to_change(self, *args):
        lst = [x for x in args][0]
        return lst

    def set_filetype(self, f):
        return f.split(".")[-1]

    def get_filepath(self):
        if self.path:
            return f'{self.path}\{self.file}'
        return self.file

    def set_mode_from_read(self):
        if self.filetype == "csv":
            return 'r'
        elif self.filetype == "json":
            return 'r'
        elif self.filetype == "pickle":
            return 'rb'

    def show_file(self):
        print(self.data)

    def lst_of_changes(self):
        lst_to_change = []
        for el in self.to_change:
            for ell in el:
                b = ell.split(",")
                c = [int(x) for x in b[:-1]]
                d = c[0], c[1], b[2]
                lst_to_change.append(d)
        return lst_to_change

    def change_file(self):
        changed_file = self.data
        changed_file[self.changes[0][0]][self.changes[0][1]] = self.changes[0][2]
        return changed_file

    def set_data(self):
        with self.to_read: # to with open ma być przekazane jako  do readline
            if hasattr(self, f'get_{self.filetype}_data'):
                return getattr(self, f'get_{self.filetype}_data')()
            print(f"Konieczna implementacja metody: get_{self.filetype}_data na {self}")
            return []

    def from_where_save_file_to(self):
        if self.filetype_to_write == "csv":
            return Csv_Manager
        elif self.filetype_to_write == "json":
            return Json_Manager
        elif self.filetype_to_write == "pickle":
            return Pickle_Manager
        else:
            raise TypeError("Nie ma metody obsługującej ten format.")
            
    def set_mode_to_write(self):
        if self.filetype_to_write == "csv":
            return 'w'
        elif self.filetype_to_write == "json":
            return 'w'
        elif self.filetype_to_write == "pickle":
            return 'wb'

    def save_file_to(self):
        with self.to_write:
            if hasattr(self, f'get_{self.filetype_to_write}_data'):
                return getattr(self, f'save_{self.filetype_to_write}_data')()
            else:
                getattr(self.from_where_save_file_to(),f'save_{self.filetype_to_write}_data')(self)
            print(f"Konieczna implementacja metody: save_{self.filetype}_data na {self}")
            return []


class Csv_Manager(File_Manager):
    def get_csv_data(self):
        data = []
        for line in self.to_read.readlines():
            data.append(line.replace("\n", "").split(";"))
        return data

    def save_csv_data(cls):
        for line in cls.changed_file:
            cls.to_write.write(str(line[0]) + ";" + str(line[1]) + "\n") 

class Json_Manager(File_Manager):
    def get_json_data(self):
        data = json.loads(self.to_read.read())
        return [[key, value] for key, value in data.items()]

    def save_json_data(cls):
        dict_of_changed_file=dict(cls.changed_file)
        json.dump(dict_of_changed_file, cls.to_write)

class Pickle_Manager(File_Manager):
    def get_pickle_data(self):
        data = pickle.load(self.to_read)
        return [[key, value] for key, value in data.items()]

    def save_pickle_data(cls):
        dict_of_changed_file=dict(cls.changed_file)
        print(type(cls.to_write))
        pickle.dump(dict_of_changed_file, cls.to_write)

class Manager(File_Manager): 
    def __new__(cls, file, file_to_write, path, *args, format=""):
        if format=="csv":
            return Csv_Manager(file, file_to_write, path, *args)
        elif format=="json":
            return Json_Manager(file, file_to_write, path, *args)
        elif format=="pickle":
            return Pickle_Manager(file, file_to_write, path, *args)
        print("Nie ma metody obsuługującej odczyt danych z tego formatu.")