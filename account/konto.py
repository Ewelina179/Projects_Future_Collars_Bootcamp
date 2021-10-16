import sys
from acc.accountant import Manager

manager = Manager(sys.argv[2:], file = sys.argv[1])

@manager.assign("konto")
def my_func(manager):
    print(f"Saldo wynosi: {manager.saldo}; stan magazynu: {manager.products}.")

my_func(manager)