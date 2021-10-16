import sys

class Manager:

    def __init__(self, *args, file):
        
        self.file = file
        self.saldo = self.get_saldo()
        self.products = self.get_products()
        self.show = self.show_file()
        self.variables = args # tupla z jednym elementem - listą
        
        self.actions = {
                    "saldo": self.change_saldo(), # bez nawiasu. wykonuje się przy execute!!!
                    "sprzedaż": "",
                    "zakup": "",
                    "konto": "",
                    "magazyn": "",
                    "przegląd": ""
                }
        self.to_file = self.save_changes()

    def change_saldo(self):
        print("Cześć!")
        change_in_account = int(self.variables[0][0])
        comment = self.variables[0][1]
        self.saldo += change_in_account*0.01
        print(f"Saldo wynosi: {self.saldo}.")

    def assign(self, name):
        def decorate(cb):
            self.actions[name] = cb # weż tę funckję? - przypisało funkcję. ale niżej się ona execute
            # bierze z tej funckji te argumenty???
            return cb
        return decorate

    def get_saldo(self):
        with open(self.file, "r") as fd:
                line = fd.readline()
                sline = line.split(";")
                main_saldo = float(sline[1])
        return main_saldo

    def get_products(self):
        products = {}
        with open(self.file, "r") as fd:
                for line in fd.readlines()[1:]:
                    splitted_line = line.split(";")
                    products[splitted_line[0]] = {"amount": int(splitted_line[1]), "price": float(splitted_line[2])}
        return products

    def show_file(self):
        print(f'Saldo to: {self.saldo} a produkty {self.products}')

    def save_changes(self):
        with open(self.file, "w") as fd:
            fd.write("saldo" + ";" + str(self.saldo) + ";" +"\n")
            for key,value in self.products.items():
                x = str(key + ";" + str(value["amount"]) + ";" + str(value["price"]) + "\n")
                fd.write(x)
    
    def execute(self, name):
        if name not in self.actions:
            print("Action not defined")
        else:
            self.actions[name]()
            print("To tutaj.")
            print(self.saldo)
            self.save_changes()
            # kiedy zapisać zmiany w pliku??????

manager = Manager(sys.argv[2:], file = sys.argv[1])
print(manager.variables)

@manager.assign("saldo") # jeżeli przyjmuje więcej argumentów to w tym miejscu przypisanie do zmiennej w assign i zgarnięcie kolejnych parametrów i dopiero w execute 
def my_func():
    with open(sys.argv[1], "r") as fd:
        products = {}
        line = fd.readline()
        sline = line.split(";")
        main_saldo = float(sline[1])
        for line in fd.readlines():
            splitted_line = line.split(";")
            products[splitted_line[0]] = {"amount": int(splitted_line[1]), "price": float(splitted_line[2])}

    print(f"Saldo wynosi: {main_saldo}; stan magazynu: {products}.") # tu niech odczyta z pliku i printować bieżący stan

my_func()
#manager.execute("saldo")  # w tym przypadku my_func ma parametr manager i to execute odpala funkcję
