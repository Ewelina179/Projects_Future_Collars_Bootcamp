import sys

from all_func import change_saldo
from my_context_manager import FileManager

magazyn_dict = {}
logs = []

file = sys.argv[1]


with FileManager(file, "r") as fd:
    line = fd.readline()
    sline = line.split(";")
    saldo = float(sline[1])

with FileManager(file, "r") as fd:
    for line in fd.readlines()[1:]:
        splitted_line = line.split(";")
        product = splitted_line[0]
        product_amount = int(splitted_line[1])
        product_price = float(splitted_line[2])
        magazyn_dict[product] = {'amount':product_amount, 'price': product_price}

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
        if change_in_account_in < 0 and abs(change_in_account_in) > saldo:
            print("Zmiana (ujemna) przekracza wartość salda. Nie można wykonać operacji.")
            continue
        else:
            change_in_account_in = float(input("Zmiana na koncie wyrażona w groszach: "))
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
                if not magazyn_dict.get(product_id):
                    magazyn_dict[product_id] = {"amount":current_amount, "price": price}
                else:
                    amount = magazyn_dict[product_id]['amount']
                    magazyn_dict[product_id]={'amount': amount + current_amount, "price": price}
                log = f"Stan magazynowy produktu {product_id} podniesiono o liczbę {current_amount}. Saldo wynosi: {saldo}" 
                logs.append(log)
                #parameters.extend([product_id, price, current_amount]
    elif answer == "sprzedaz":
        product_id = input("Podaj identyfikator produktu: ")
        price = float(input("Podaj cenę jednostkową: "))
        current_amount = int(input("Podaj liczbę sztuk: "))

        if price < 0 or current_amount < 0:
            print("Liczba sprzedanych sztuk nie może być ujemna. Cena produktu nie może być ujemna.")
            continue
        if not magazyn_dict.get(product_id):
            print(f"W magazynie nie ma takiego produktu: {product_id}")
            continue
        else:
            if magazyn_dict[product_id]['amount'] < current_amount:
                print("Brak wystarczającej liczby sztuk produktu.")
                continue
            else:
                saldo += price * current_amount
                amount = magazyn_dict[product_id]['amount']
                magazyn_dict[product_id]={'amount': amount - current_amount, 'price': price}
                log = f"Stan magazynowy produktu {product_id} zmniejszono o liczbę {current_amount}. Saldo wynosi: {saldo}." 
                print(log)
                logs.append(log)
                #parameters.extend([product_id, price, current_amount])

for el in sys.argv[2:]:
        x = magazyn_dict.get(el)
        if x:
            print(f"Stan magazynowy dla produktu {el} wynosi: {x['amount']}.")
        else:
            print(f"Nie ma wskazanego produktu: {el}.")


with FileManager("warehouse.txt", "w") as fd:
    fd.write("saldo" + ";" + str(saldo) + ";" +"\n")
    for key, value in magazyn_dict.items():
        x = str(key) + ";" + str(value['amount']) + ";" + str(value['price']) + "\n"
        fd.write(x)

with FileManager("logs.txt", "a") as fd:
    for el in logs:
        fd.write(el)

with FileManager("parameters", "a"):
    pass
