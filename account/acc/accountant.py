import sys

class Manager:

    def __init__(self, *args, file):
        
        self.file = file
        self.saldo = self.get_saldo()
        self.products = self.get_products()
        #self.show = self.show_file()
        self.variables = args # tupla z jednym elementem - listą
        
        self.actions = {
                    "saldo": self.change_saldo, # bez nawiasu. wykonuje się przy execute!!!
                    "sprzedaz": self.sale,
                    "zakup": self.purchase,
                    "konto": self.account,
                    "magazyn": self.current_amount,
                    "przegląd": "dodać logi"
                }
        self.to_file = self.save_changes()

    def change_saldo(self):
        print("Cześć!")
        change_in_account = int(self.variables[0][0])
        comment = self.variables[0][1]
        self.saldo += change_in_account*0.01
        print(f"Saldo wynosi: {self.saldo}.")

    def sale(self):
        print("Cześć, tu sprzedaż!")
        product_id = str(self.variables[0][0])
        price = int(self.variables[0][1])
        amount = int(self.variables[0][2])
        self.saldo += price * amount
        self.products[product_id]['amount'] -= amount
        print(f"Stan konta: {self.saldo}, stan magazynu: {self.products}")

    def purchase(self):
        print("Cześć, tu zakup!")
        product_id = str(self.variables[0][0])
        price = int(self.variables[0][1])
        amount = int(self.variables[0][2])
        self.saldo -= price * amount
        self.products[product_id]['amount'] += amount
        print(f"Stan konta: {self.saldo}, stan magazynu: {self.products}")

    def account(self):
        print(f"Stan konta to: {self.saldo}.")

    def current_amount(self):
        for el in self.variables[0]:
            product_name = el
            amount = self.products[product_name]['amount']
            print(f"Stan magazynowy produktu: {amount}")

    def assign(self, name):
        def decorate(func):
            self.actions[name]() # weż tę funckję? - przypisało funkcję. ale niżej się ona execute
            # bierze z tej funckji te argumenty???
            self.save_changes()
            return func
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
    
    def execute(self, name): # w sumie to nie używam. nie ogarniam.
        if name not in self.actions:
            print("Action not defined")
        else:
            # self.actions[name](self)
            print("To tutaj.")
            self.save_changes()