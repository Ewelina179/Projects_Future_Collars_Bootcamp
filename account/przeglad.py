import sys
from acc.accountant import Manager

manager = Manager(file = sys.argv[1])

@manager.assign("przeglad")
def my_func(manager):
    print(f"Saldo wynosi: {manager.saldo}; stan magazynu: {manager.products}.")

my_func(manager)