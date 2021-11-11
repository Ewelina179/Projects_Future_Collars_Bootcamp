from db import db
from datetime import datetime

class Saldo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(), default=datetime.utcnow)
    value = db.Column(db.Integer, nullable=False)

    def __str__(self):
        actual_saldo = db.session.query(self).filter(self.value).order_by((self.date.desc())).first()
        x = actual_saldo.value
        print(x)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def show_products(self):
        return db.session.query(self).all()


class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(), default=datetime.utcnow)
    content = db.Column(db.Text(), nullable=False)

    def show_history(self):
        pass

    def show_history_from_to(self):
        pass


class Manager:

    def add_comment(self, com):
        x = History(content=com)
        db.session.add(x)
        db.session.commit()

    def save_to_db(self, sth):
        db.session.add(sth)
        db.session.commit()

    def commit_changes_in_saldo(self, value, comment):
        x = f"Saldo wynosi: {value}, komentarz do zmiany: {comment}"
        self.add_comment(x)

    def commit_changes_sale(self, product_id, price, amount):
        x = f"Sprzedano produkt: {product_id}, w cenie: {price}, w ilości {amount}."
        self.add_comment(x)

    def commit_changes_purchase(self, product_id, price, amount):
        x = f"Zakupiono produkt: {product_id}, w cenie: {price}, w ilości: {amount}"
        self.add_comment(x)

    def change_saldo(self, change_in_account, comment):
        saldo = db.session.query(Saldo).filter(Saldo.value).order_by((Saldo.date.desc())).first()
        print(saldo.date)
        print(saldo.value)
        saldo.value += round(change_in_account*0.01, 2)
        self.save_to_db(saldo)
        self.commit_changes_in_saldo(saldo.value, comment)

    def sale(self, product_id, price, amount):
        saldo = db.session.query(Saldo).filter(Saldo.value).order_by((Saldo.date.desc())).first()
        saldo.value += price * amount
        # gdzie nazwa produktu jest taka w bazie to go zmień
        product = db.session.query(Product).filter(Product.name == product_id).first() # chyba źle query
        product.amount -= amount
        self.save_to_db(saldo)
        self.save_to_db(product)
        self.commit_changes_sale(product_id, price, amount)

    def purchase(self, product_id, price, amount):
        saldo = db.session.query(Saldo).filter(Saldo.value).order_by((Saldo.date.desc())).first()
        saldo.value -= price * amount
        product = self.db.session.query(self.product.name == product_id).first()
        product.amount += amount
        self.save_to_db(saldo)
        self.save_to_db(product)
        self.commit_changes_purchase(product_id, price, amount)