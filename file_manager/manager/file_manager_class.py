import csv

class File_Manager:
    def init(self, file):
        self.file = file
        pass

    def show_file(self):
        print(self.read_file())

    def change_file(self, to_change):
        lst_to_change = []
        for el in to_change:
            b = el.split(",")
            c = [int(x) for x in b[:-1]]
            d = c[0], c[1], b[2]
            lst_to_change.append(d)
        return lst_to_change
        
    
class Csv_Manager(File_Manager):
    def init(self, file):
        super().__init__()
        self.file_to_write = file

    def read_file(self):
        content_of_file = []
        with open(self.file, newline="") as f:
            reader = csv.reader(f)
            for line in reader:
                content_of_file.append(line)
        return content_of_file

    def save_to_file(self, to_change):
        x = self.change_file(to_change) # [0,0,'A']
        y = self.read_file()
        #self.read_file()[x[0]][x[1]]= x[2]
        y[0][0] = 'A' # podmieniam plik
        print(y)

        with open(self.file_to_write, 'w', newline="") as f: 
            csvwriter = csv.writer(f) 
            csvwriter.writerows(y) 


class Json_Manager(File_Manager):
    def init(self, file):
        super().__init__()
        self.file_to_write = file
    
    def save_to_file():
        pass

class Pickle_Manager(File_Manager):
    def init(self, file):
        super().__init__()
        self.file_to_write = file

    def save_to_file():
        pass 


class Manager(File_Manager):
    def init(self):
        super().__init__()

    def __new__(cls, c=False, j=False, p=False): 
        if c:
            return Csv_Manager()
            super().__new__(cls, field)
        elif j:
            return Json_Manager()
        elif p:
            return Pickle_Manager()


# jest klasa bazowa. pozostałe dziedziczą po niej metody i nadpisują, jak trzeba