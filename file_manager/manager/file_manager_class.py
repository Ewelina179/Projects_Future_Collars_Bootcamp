import csv, json

class File_Manager:
    def init(self, file):
        self.file = file

    def show_file(self):
        print(self.read_file_from())

    def change_file(self, to_change):
        lst_to_change = []
        for el in to_change:
            b = el.split(",")
            c = [int(x) for x in b[:-1]]
            d = c[0], c[1], b[2]
            lst_to_change.append(d)
        return lst_to_change

    def read_file_from(self):
        if self.file[-4:] == ".csv":
            print("yes")
            return Csv_Manager.read_file(self)
        elif self.file[-5:] == ".json":
            return Json_Manager.read_file(self)
        elif self.file[-7:] == ".pickle":
            return Pickle_Manager.read_file(self)
    

class Csv_Manager(File_Manager):
    def init(self, file):
        super().__init__()
        self.file_to_write = file

    def read_file_from(self):
        return super().read_file_from()
    
    def read_file(self):
        content_of_file = []
        with open(self.file, newline="") as f:
            reader = csv.reader(f)
            for line in reader:
                content_of_file.append(line)
        return content_of_file

    def save_to_file(self, to_change):
        x = self.change_file(to_change)[0]
        y = self.read_file_from()
        y[x[0]][x[1]]= x[2]

        with open(self.file_to_write, 'w', newline="") as f: 
            csvwriter = csv.writer(f) 
            csvwriter.writerows(y) 


class Json_Manager(File_Manager):
    def init(self, file):
        super().__init__()
        self.file_to_write = file

    def read_file_from(self):
        return super().read_file_from()

    def read_file(self):
        content_of_file = []
        with open(self.file, newline="") as f:
            data = json.load(f)
            for line in data:
                content_of_file.append(line)
        return content_of_file
    
    def save_to_file(self, to_change):
        x = self.change_file(to_change)[0]
        y = self.read_file_from()
        y[x[0]][x[1]]= x[2]

        with open(self.file_to_write, 'w', newline="") as f: 
            pass


class Pickle_Manager(File_Manager):
    def init(self, file):
        super().__init__()
        self.file_to_write = file
    
    def read_file_from(self):
        return super().read_file_from()

    def read_file(self):
        content_of_file = []
        with open(self.file, newline="") as f:
            reader = csv.reader(f)
            for line in reader:
                content_of_file.append(line)
        return content_of_file

    def save_to_file(self, to_change):
        x = self.change_file(to_change)[0]
        y = self.read_file_from()
        y[x[0]][x[1]]= x[2]

        with open(self.file_to_write, 'w', newline="") as f: 
            pass 


class Manager(File_Manager):
    def init(self):
        super().__init__()

    def __new__(cls, c=False, j=False, p=False): 
        if c:
            return Csv_Manager()
        elif j:
            return Json_Manager()
        elif p:
            return Pickle_Manager()
