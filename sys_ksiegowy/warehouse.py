class Product:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price

    def change_amount(self, new_amount):
        self.amount += new_amount

    def __repr__(self):
        return self.name


class Warehouse:
    def __init__(self, products = None):
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)

    def lst_of_product_names(self):
        lst = []
        for product in self.products:
            lst.append(product.name)
        return lst

main_warehouse = Warehouse()

