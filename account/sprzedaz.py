import sys
from acc.accountant import Manager

manager = Manager(sys.argv[2:], file = sys.argv[1])
print(manager.variables)

@manager.assign("sprzedaz")
def my_func():
    with open(sys.argv[1], "r") as fd:
        products = {}
        line = fd.readline()
        sline = line.split(";")
        main_saldo = float(sline[1])
        for line in fd.readlines():
            splitted_line = line.split(";")
            products[splitted_line[0]] = {"amount": int(splitted_line[1]), "price": float(splitted_line[2])}

    print(f"Saldo wynosi: {main_saldo}; stan magazynu: {products}.") # tu niech odczyta z pliku i printować bieżący stan

my_func()