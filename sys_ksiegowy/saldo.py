import sys
from operator import attrgetter

from my_context_manager import FileManager
from warehouse import Product, Warehouse, main_warehouse

from all_func import change_saldo

warehouse_dict = {}
logs = []

file = sys.argv[1]
change_in_account = int(sys.argv[2])

with FileManager(file, "r") as fd:
    line = fd.readline()
    sline = line.split(";")
    saldo = float(sline[1])


with FileManager(file, "r") as fd:
    for line in fd.readlines()[1:]:
        splitted_line = line.split(";")
        product = Product( name = splitted_line[0], amount = int(splitted_line[1]), price = float(splitted_line[2]))
        main_warehouse.add_product(product)

print(main_warehouse.products)

with FileManager("logs.txt", "r") as fd:
    for line in fd.readlines():
        logs.append(line)

COMMANDS = "saldo.py", "sprzedaz.py", "zakup.py", "konto.py", "magazyn.py", "przeglad.py"

argument = sys.argv[0]

while argument in COMMANDS:

    INNER_COMMANDS = "saldo", "zakup", "sprzedaz", "stop"

    answer = input(f"Podaj komendę z dostepnych: {INNER_COMMANDS}") 

    if answer not in INNER_COMMANDS:
        print("Niewłaściwa komenda.")
        continue

    if answer == "stop":
        break

    elif answer == "saldo":
        change_in_account_in = float(input("Zmiana na koncie wyrażona w groszach: "))
        if change_in_account_in < 0 and abs(change_in_account_in) > saldo:
            print("Zmiana (ujemna) przekracza wartość salda. Nie można wykonać operacji.")
            continue
        else:
            saldo += change_in_account_in * 0.01
            comment = input("Komentarz do zmiany: ")
            log = f"Zmieniono wartość salda o {change_in_account_in * 0.01} złotych. Saldo po zmianie wynosiło {saldo}."
            logs.append(log)
            #parameters.append(change_in_account)
            #parameters.append(comment)
        
    elif answer == "zakup":
        product_id = input("Podaj identyfikator produktu: ")
        price = float(input("Podaj cenę jednostkową: "))
        current_amount = int(input("Podaj liczbę sztuk: "))
        if price < 0 or current_amount < 0:
            print("Liczba sztuk nie może być mniejsza od 0. Cena nie może być ujemna.")
            continue
        else:
            total_price = price * current_amount
            if saldo < total_price:
                print("Saldo nie może być ujemne.")
                continue
            else:
                saldo -= total_price
                if product_id not in main_warehouse.lst_of_product_names():
                    product = (product_id, current_amount, price)
                    main_warehouse.add_product(product)
                else:
                    product = [x for x in main_warehouse.products if x.name == product_id][0]
                    product.change_amount(current_amount)
                log = f"Stan magazynowy produktu {product} podniesiono o liczbę {current_amount}. Saldo wynosi: {saldo}" 
                logs.append(log)
                #parameters.extend([product_id, price, current_amount]) # czy program ma zapisywać wszystkie parametry, czy tylko te, które miały wpływ na saldo? nie do końca rozumiem punkt V. właściwie wcale nie rozumiem.

    elif answer == "sprzedaz":
        product_id = input("Podaj identyfikator produktu: ")
        price = float(input("Podaj cenę jednostkową: "))
        current_amount = int(input("Podaj liczbę sztuk: "))

        if price < 0 or current_amount < 0:
            print("Liczba sprzedanych sztuk nie może być ujemna. Cena produktu nie może być ujemna.")
            continue
        if product_id not in main_warehouse.lst_of_product_names():
            print(f"W magazynie nie ma takiego produktu: {product_id}")
            continue
        else:
            product = [x for x in main_warehouse.products if x.name == product_id][0]
            if product.amount < current_amount:
                print("Brak wystarczającej liczby sztuk produktu.")
                continue
            else:
                saldo += price * current_amount
                product.change_amount(-current_amount)
                log = f"Stan magazynowy produktu {product.name} zmniejszono o liczbę {current_amount}. Saldo wynosi: {saldo}." 
                print(log)
                logs.append(log)
                #parameters.extend([product_id, price, current_amount])

if change_in_account < 0 and abs(change_in_account) > saldo:
    print("Zmiana (ujemna) przekracza wartość salda. Nie można wykonać operacji.")
else:
    new_saldo = str(change_saldo(change_in_account, saldo)) # nie jestem pewna czy to w tym miejscu. 
    log = f"Zmieniono wartość salda o {change_in_account * 0.01} złotych. Saldo po zmianie wynosiło {new_saldo}."
    logs.append(log)
    print(log)
    with FileManager("warehouse.txt", "w") as fd:
        fd.write("saldo" + ";" + new_saldo + ";" +"\n")
        for product in main_warehouse.products:
            x = str(product.name) + ";" + str(product.amount) + ";" + str(product.price) + "\n"
            fd.write(x)


with FileManager("logs.txt", "w") as fd:
    for el in logs:
        fd.write(el) # z trybem "a" za każdym razem czytało cały plik i w tym momencie go dopisywało. stąd taki rozmiar pliku.

with open ("parameters", "a"):
    pass
