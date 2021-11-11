from flask import Flask, render_template, request, redirect, url_for
from flask_migrate import Migrate
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
    z = db.session.query(Saldo).filter(Saldo.value).order_by((Saldo.date.desc())).first()
    #saldo = Saldo() coś nie działa ;p
    saldo = z.value
    #print(Saldo())
    #products = Product().show_products()
    product = db.session.query(Product).all()
    for el in product:
        print(el.amount)

    if formSaldo.validate_on_submit():
        manager.change_saldo(formSaldo.value.data, formSaldo.comment.data)
        return redirect(url_for('home'))
    elif formSale.validate_on_submit():
        manager.sale(formSale.name.data, formSale.price.data, formSale.amount.data)
        return redirect(url_for('home'))
    elif formPurchase.validate_on_submit():
        manager.purchase(formPurchase.name.data, formPurchase.price.data, formPurchase.amount.data)
        return redirect(url_for('home'))
    
    return render_template("index.html", saldo=saldo, magazyn=product, formSale=formSale, formPurchase=formPurchase, formSaldo=formSaldo)

@app.route('/history', defaults={'line_from': None, 'line_to': None})
@app.route('/history/<int:line_from>/<int:line_to>')
def history(line_from, line_to):
    history = History()
    magazyn = Manager()
    if line_from and line_to:
        logs = magazyn.logs[(line_from-1):(line_to)]
    else:
        logs = magazyn.logs
    return render_template("history.html", logs=logs)

if __name__ == '__main__':
    app.run(debug=True)
