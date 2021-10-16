import sys
from acc.accountant import Manager

manager = Manager(sys.argv[2:], file = sys.argv[1])

@manager.assign("przeglad")
def my_func(manager):
    print(f"Saldo wynosi: {manager.saldo}; stan magazynu: {manager.products}.") # tu niech odczyta z pliku i printować

my_func(manager)