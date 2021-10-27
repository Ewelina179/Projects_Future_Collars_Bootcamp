class Manager:
    def __init__(self, *args, file = "accountant.txt", file_logs="logs.txt"):
        self.file = file
        self.file_logs = file_logs
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

    def validate_change_in_account(self, change):
        try:
            return float(change)
        except ValueError:
            return None

    def validate_amount(self, amount):
        try:
            return int(amount)
        except ValueError:
            return None

    def check_is_product(self, product_id):
        try:
            return self.products[product_id]
        except:
            return None

    def is_available_product(self, product_id, amount):
        if self.products[product_id]['amount'] >= amount:
            return True
        return False

    def change_saldo(self, change_in_account, comment):
        change_in_account = self.validate_change_in_account(change_in_account)
        if change_in_account and comment:
            self.saldo += round(change_in_account*0.01, 2)
            x = f"Saldo wynosi: {self.saldo}, komentarz do zmiany: {comment}"
            self.logs.append(x)
            return x
        return "Podano niepoprawne dane."

    def sale(self, product_id, price, amount):
        validated_product_id = self.check_is_product(product_id)
        validated_price = self.validate_change_in_account(price)
        validated_amount = self.validate_amount(amount)
        if validated_product_id and validated_price and validated_amount:
            if self.is_available_product(product_id, validated_amount):
                self.saldo += validated_price * validated_amount
                self.products[product_id]['amount'] -= validated_amount
                x = f"Sprzedano produkt: {product_id}, w cenie: {price}, w ilości {amount}."
                self.logs.append(x)
                return x
            return "Brak wystarczającej ilości produktów."
        return "Podano niepoprawne dane."

    def purchase(self, product_id, price, amount):
        validated_product_id = self.check_is_product(product_id)
        validated_price = self.validate_change_in_account(price)
        validated_amount = self.validate_amount(amount)
        if validated_product_id and validated_price and validated_amount:
            self.saldo -= validated_price * validated_amount
            self.products[product_id]['amount'] += validated_amount
            x = f"Zakupiono produkt: {product_id}, w cenie: {price}, w ilości: {amount}"
            self.logs.append(x)
            return x
        return "Podano niepoprawne dane."

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
                    logs.append(splitted_line[0])
        return logs

    def show_logs(self):
        print(f'Historia wprowadzonych zmian: {self.logs}')

    def save_changes(self):
        with open(self.file, "w") as fd:
            fd.write("saldo" + ";" + str(self.saldo) + ";" +"\n")
            for key,value in self.products.items():
                x = str(key + ";" + str(value["amount"]) + ";" + str(value["price"]) + ";" + "\n")
                fd.write(x)

    def save_logs(self):
        with open(self.file_logs, "w") as fd:
            for el in self.logs:
                x = str(str(el) + ";" + "\n")
                fd.write(str(x))

