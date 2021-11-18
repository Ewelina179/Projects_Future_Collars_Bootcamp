from flask_wtf import FlaskForm
from wtforms.validators import ValidationError
from wtforms.fields.core import IntegerField, StringField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired

from models import Saldo, Product
    
class SaldoForm(FlaskForm):
    value = IntegerField('Value', validators=[DataRequired()])
    comment = StringField('Comment', validators=[DataRequired()])
    submit = SubmitField('Zmień saldo.')

    def validate_value(form, value):
        saldo = Saldo.query.filter(Saldo.value).order_by(Saldo.date.desc()).first()
        value = value.data
        if saldo.value - value < 0:
            raise ValidationError("Brak wystarczającej ilości środków na koncie.")

def is_product(form, field):
    x = Product.query.filter_by(name=field.data).first()
    if not x:
        raise ValidationError("Brak produktu.")

class SaleForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), is_product])
    price = IntegerField('Price', validators=[DataRequired()])
    amount = IntegerField('Amount', validators=[DataRequired()])
    submit = SubmitField('Sprzedaż')

    def validate_amount(form, amount):
        x = Product.query.filter_by(name=form.name.data).first()
        amount=amount.data
        if x and x.amount <= amount: # inaczej warunkować?
            raise ValidationError('Brak wystarczającej ilości produktu.')

class PurchaseForm(FlaskForm):
    namep = StringField('Name', validators=[DataRequired(), is_product])
    pricep = IntegerField('Price', validators=[DataRequired()])
    amountp = IntegerField('Amount', validators=[DataRequired()])
    submitp = SubmitField('Zakup')

    def validate_amount(form, amount):
        x = Product.query.filter_by(name=form.name.data).first()
        saldo = Saldo.query.filter(Saldo.value).order_by(Saldo.date.desc()).first()
        amount=amount.data
        price=form.price.data
        if x and amount*price >= saldo.value:
            raise ValidationError('Brak wystarczających środków na koncie.')