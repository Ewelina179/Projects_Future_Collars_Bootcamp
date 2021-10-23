class Manager:

    def __init__(self, *args, file):
        self.file = file
        self.file_logs = 'logs.txt'
        self.saldo = self.get_saldo()
        self.products = self.get_products()
        self.logs = self.get_logs()
        self.variables = args 
        self.actions = {
                    "saldo": self.change_saldo,
                    "sprzedaz": self.sale,
                    "zakup": self.purchase,
                    "konto": self.account,
                    "magazyn": self.current_amount,
                    "przeglad": self.show_logs
                }
        self.to_file = self.save_changes()

    def change_saldo(self):
        change_in_account = int(self.variables[0][0])
        comment = self.variables[0][1]
        self.saldo += round(change_in_account*0.01, 2)
        x = f"Saldo wynosi: {self.saldo}, komentarz do zmiany: {comment}"
        self.logs.append(x)

    def sale(self):
        product_id = str(self.variables[0][0])
        price = int(self.variables[0][1])
        amount = int(self.variables[0][2])
        self.saldo += price * amount
        self.products[product_id]['amount'] -= amount
        x = f"Dodano produkt: {product_id}, w cenie: {price}, w ilości {amount}."
        self.logs.append(x)

    def purchase(self):
        product_id = str(self.variables[0][0])
        price = int(self.variables[0][1])
        amount = int(self.variables[0][2])
        self.saldo -= price * amount
        self.products[product_id]['amount'] += amount
        x = f"Stan konta: {self.saldo}, stan magazynu: {self.products}"
        self.logs.append(x)

    def account(self):
        print(f"Stan konta to: {self.saldo}.")

    def current_amount(self):
        for el in self.variables[0]:
            product_name = el
            amount = self.products[product_name]['amount']
            print(f"Stan magazynowy produktu: {amount}")

    def assign(self, name):
        def decorate(func):
            self.actions[name]()
            self.save_changes()
            self.save_logs()
            return func
        return decorate

    def get_saldo(self):
        with open(self.file, "r") as fd:
                line = fd.readline()
                sline = line.split(";")
                main_saldo = float(sline[1])
        return round(main_saldo,2)

    def get_products(self):
        products = {}
        with open(self.file, "r") as fd:
                for line in fd.readlines()[1:]:
                    splitted_line = line.split(";")
                    products[splitted_line[0]] = {"amount": int(splitted_line[1]), "price": float(splitted_line[2])}
        return products

    def get_logs(self):
        logs = []
        with open(self.file_logs, "r") as fd:
                for line in fd.readlines():
                    splitted_line = line.split(";")
                    logs.append(splitted_line[0] + "\n")
        return logs

    def show_logs(self):
        print(f'Historia wprowadzonych zmian: {self.logs}')

    def save_changes(self):
        with open(self.file, "w") as fd:
            fd.write("saldo" + ";" + str(self.saldo) + ";" +"\n")
            for key,value in self.products.items():
                x = str(key + ";" + str(value["amount"]) + ";" + str(value["price"]) + "\n")
                fd.write(x)

    def save_logs(self):
        with open(self.file_logs, "w") as fd:
            for el in self.logs:
                x = str(el)
                fd.write(str(x))