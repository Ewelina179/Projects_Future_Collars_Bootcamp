from flask import Flask, render_template, request
from flask_migrate import Migrate
from models import Saldo, Product, History, Manager
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db.init_app(app)
migrate = Migrate(app, db)
manager = Manager()

@app.route('/')
def hello_world():
    manager.change_saldo(100, "zmiana1")
    x = db.session.query(Saldo.value).order_by(Saldo.date).all()[-1]
    print(x)
    z = db.session.query(Saldo).filter(Saldo.value).order_by((Saldo.date.desc())).first()
    print(z)
    #manager.sale("Produkt1", 1, 1)
    #z = db.session.query(Product).all()
    #print(z)
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
