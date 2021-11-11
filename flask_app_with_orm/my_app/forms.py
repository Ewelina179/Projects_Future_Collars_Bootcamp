from flask_wtf import FlaskForm
from wtforms import ValidationError
from wtforms.fields.core import IntegerField, StringField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired

from models import Saldo, Product

class SaldoForm(FlaskForm):
    value = IntegerField('Value', validators=[DataRequired()])
    comment = StringField('Comment', validators=[DataRequired()])
    submit = SubmitField('Zmień saldo.')

    def check_is_enough(self, field):
        pass

class SaleForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    amount = IntegerField('Amount', validators=[DataRequired()])
    submit = SubmitField('Zakup')

    def is_available_product(self, field):
        x = Product.query.filter_by(name=field.data.name).first()
        if x.amount >= field.data.amount:
            raise ValidationError('Brak wystarczającej ilości produktu.')

    def is_product(self, field):
        x = Product.query.filter_by(name=field.data.name).first()
        if not x:
            raise ValidationError('Brak produktu o podanej nazwie.')

class PurchaseForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    amount = IntegerField('Amount', validators=[DataRequired()])
    submit = SubmitField('Sprzedaż')

    def check_is_enough_money_to_buy(self, field):
        pass
