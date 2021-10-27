from flask import Flask, render_template, request, url_for, redirect
from manager import Manager

app = Flask(__name__)


@app.route('/', methods = ["GET", "POST"])
def home():
    manager = Manager()
    
    zakup = {
        "product_name": request.form.get("Z_product_name"),
        "price": request.form.get("Z_price"),
        "amount": request.form.get("Z_liczba")
    }
    
    sprzedaz = {
        "product_name": request.form.get("S_product_name"),
        "price": request.form.get("S_price"),
        "amount": request.form.get("S_liczba")
    }
    
    saldo = {
        "saldo_comment" : request.form.get("saldo_comment"),
        "saldo_amount" : request.form.get("saldo_amount")
    }

    def switching():
        if zakup["product_name"]:
            return manager.purchase(zakup["product_name"], zakup["price"], zakup["amount"])
        elif sprzedaz["product_name"]:
            return manager.sale(sprzedaz["product_name"], sprzedaz["price"], sprzedaz["amount"])
        elif saldo["saldo_amount"]:
            return manager.change_saldo( saldo["saldo_amount"], saldo["saldo_comment"])

    comment = switching()
    manager.save_changes()
    manager.save_logs()
    return render_template("index.html", saldo=manager.saldo, magazyn=manager.products, comment=comment)


@app.route('/history', defaults={'line_from': None, 'line_to': None})
@app.route('/history/<int:line_from>/<int:line_to>')
def history(line_from, line_to):
    magazyn = Manager()
    if line_from and line_to:
        logs = magazyn.logs[(line_from-1):(line_to)]
    else:
        logs = magazyn.logs
    return render_template("history.html", logs=logs)


