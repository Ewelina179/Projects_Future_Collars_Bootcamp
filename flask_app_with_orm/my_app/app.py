from flask import Flask, render_template, request, redirect, url_for, flash
from flask_migrate import Migrate
from flask_wtf import form
from models import Saldo, Product, History, Manager
from db import db
from forms import SaldoForm, PurchaseForm, SaleForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] = "SECRET_KEY"

db.init_app(app)
migrate = Migrate(app, db)
manager = Manager()
@app.route('/', methods=['GET', 'POST'])
def home():
    formSaldo = SaldoForm()
    formSale = SaleForm()
    formPurchase = PurchaseForm()
    saldo = Saldo().show_actual_saldo()
    magazyn = Product().show_products()

    if request.method == 'POST':
        if formSaldo.validate_on_submit():
            print('saldo')
            manager.change_saldo(formSaldo.value.data, formSaldo.comment.data)
            return redirect(url_for('home'))
        else:
            flash(formSaldo.errors)
        if formSale.validate_on_submit():
            print("s")
            manager.sale(formSale.name.data, formSale.price.data, formSale.amount.data)
            return redirect(url_for('home'))
        else:
            flash(formSale.errors)
        if formPurchase.validate_on_submit():
            print("p")
            manager.purchase(formPurchase.namep.data, formPurchase.pricep.data, formPurchase.amountp.data)
            return redirect(url_for('home'))
        else:
            flash(formPurchase.errors)
    return render_template("index.html", saldo=saldo, product=magazyn, formSale=formSale, formPurchase=formPurchase, formSaldo=formSaldo)

@app.route('/history', defaults={'line_from': None, 'line_to': None})
@app.route('/history/<int:line_from>/<int:line_to>')
def history(line_from, line_to):
    history = History()
    if line_from and line_to:
        logs = history.show_history_from_to(line_from, line_to)
    else:
        logs = history.show_history()
    return render_template("history.html", logs=logs)

if __name__ == '__main__':
    app.run(debug=True)
