from flask import Flask, render_template, request, url_for, redirect
from manager import Manager

app = Flask(__name__)


@app.route('/', methods = ["GET", "POST"])
def home():
    manager = Manager()
    print(manager.saldo)
    print(manager.products)
    print(manager.variables)

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

    if zakup["product_name"]:
        manager.variables = ((zakup["product_name"], zakup["price"], zakup["amount"]))
        x = "zakup"
        @manager.assign(x)
        def my_func(manager):
            manager.save_changes()
            manager.save_logs()
            return render_template("index.html", saldo=manager.saldo, magazyn=manager.products)
        my_func(manager)
    if sprzedaz["product_name"]:
        manager.variables = ((sprzedaz["product_name"], sprzedaz["price"], sprzedaz["amount"]))
        x = "sprzedaz"
        @manager.assign(x)
        def my_func(manager):
            manager.save_changes()
            manager.save_logs()
            return render_template("index.html", saldo=manager.saldo, magazyn=manager.products)
        my_func(manager)
    if saldo["saldo_amount"]:
        manager.variables = ((saldo["saldo_comment"], saldo["saldo_amount"]))
        x = "saldo"
        @manager.assign(x)
        def my_func(manager):
            manager.save_changes()
            manager.save_logs()
            return render_template("index.html", saldo=manager.saldo, magazyn=manager.products)
        my_func(manager)
    else:
        return render_template("index.html", saldo=manager.saldo, magazyn=manager.products)


@app.route('/history', defaults={'line_from': None, 'line_to': None})
@app.route('/history/<line_from>/<line_to>')
def history(line_from, line_to):
    magazyn = Manager()
    if line_from and line_to:
        logs = magazyn.logs[int(line_from):int(line_to)+1]
    else:
        logs = magazyn.logs
    return render_template("history.html", logs=logs)

