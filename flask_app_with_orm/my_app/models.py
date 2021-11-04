from db import db
from datetime import datetime

class Saldo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(), default=datetime.utcnow)
    value = db.Column(db.Integer, nullable=False)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)

class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(), default=datetime.utcnow)
    content = db.Column(db.Text(), nullable=False)


class Manager:
    def __init__(self):
        pass

    def add_comment(self, com):
        x = History(content=com)
        db.session.add(x)
        db.session.commit()

    def save_sth(self, sth):
        db.session.add(sth)
        db.session.commit()

    def change_saldo(self, change_in_account, comment):
        #change_in_account = self.validate_change_in_account(change_in_account)
        if change_in_account and comment:
            saldo = db.session.query(Saldo).filter(Saldo.value).order_by((Saldo.date.desc())).first()
            print(saldo.date)
            print(saldo.value)
            #me = db.session.query(User).filter(Customer.username=="robergo").first()
            #me.lastname = "Coś"
            saldo.value += round(change_in_account*0.01, 2)
            self.save_sth(saldo)
            x = f"Saldo wynosi: {saldo.value}, komentarz do zmiany: {comment}"
            self.add_comment(x)
            return x
        return "Podano niepoprawne dane."

    def sale(self, product_id, price, amount):
        validated_product_id = self.check_is_product(product_id)
        validated_price = self.validate_change_in_account(price)
        validated_amount = self.validate_amount(amount)
        if validated_product_id and validated_price and validated_amount:
            if self.is_available_product(product_id, validated_amount):
                saldo = db.session.query(Saldo).filter(Saldo.value).order_by((Saldo.date.desc())).first()
                saldo += validated_price * validated_amount
                self.save_saldo(saldo)
                # gdzie nazwa produktu jest taka w bazie to go zmień
                product = db.session.query(Product.name == product_id).first()
                product.amount -= validated_amount
                self.save_sth(product)
                x = f"Sprzedano produkt: {product_id}, w cenie: {price}, w ilości {amount}."
                self.add_comment(x)
                return x
            return "Brak wystarczającej ilości produktów."
        return "Podano niepoprawne dane."

    def purchase(self, product_id, price, amount):
        validated_product_id = self.check_is_product(product_id)
        validated_price = self.validate_change_in_account(price)
        validated_amount = self.validate_amount(amount)
        if validated_product_id and validated_price and validated_amount:
            saldo = db.session.query(Saldo).filter(Saldo.value).order_by((Saldo.date.desc())).first() # saldo gdzieś na górze czy na bieżąco? za długie to wszystko
            saldo -= validated_price * validated_amount
            self.save_saldo(saldo)
            product = self.db.session.query(self.product.name == product_id).first()
            product.amount += validated_amount
            self.save_sth(product)
            x = f"Zakupiono produkt: {product_id}, w cenie: {price}, w ilości: {amount}"
            self.add_comment(x)
            return x
        return "Podano niepoprawne dane."

    def current_amount(self):
        for el in self.variables[0]:
            product_name = el
            amount = self.products[product_name]['amount']
            print(f"Stan magazynowy produktu: {amount}")