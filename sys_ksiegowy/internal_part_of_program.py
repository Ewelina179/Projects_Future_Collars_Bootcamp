from const import COMMANDS, INNER_COMMANDS
from warehouse import main_warehouse

import work_with_context_manager

def get_command(argument):
    while argument in COMMANDS:

        answer = input(f"Podaj komendę z dostepnych: {INNER_COMMANDS}") 

        if answer not in INNER_COMMANDS:
            print("Niewłaściwa komenda.")
            continue

        if answer == "stop":
            break

        elif answer == "saldo":
            change_in_account_in = float(input("Zmiana na koncie wyrażona w groszach: "))
            if change_in_account_in < 0 and abs(change_in_account_in) > work_with_context_manager.main_saldo:
                print("Zmiana (ujemna) przekracza wartość salda. Nie można wykonać operacji.")
                continue
            else:
                work_with_context_manager.main_saldo += change_in_account_in * 0.01
                comment = input("Komentarz do zmiany: ")
                log = f"Zmieniono wartość salda o {change_in_account_in * 0.01} złotych. Saldo po zmianie wynosiło {work_with_context_manager.main_saldo}."
                work_with_context_manager.logs.append(log)
                print(work_with_context_manager.logs[-1])
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
                if work_with_context_manager.main_saldo < total_price:
                    print("Saldo nie może być ujemne.")
                    continue
                else:
                    work_with_context_manager.main_saldo -= total_price
                    if product_id not in work_with_context_manager.main_warehouse.lst_of_product_names():
                        product = (product_id, current_amount, price)
                        work_with_context_manager.main_warehouse.add_product(product)
                    else:
                        product = [x for x in main_warehouse.products if x.name == product_id][0]
                        product.change_amount(current_amount)
                    log = f"Stan magazynowy produktu {product} podniesiono o liczbę {current_amount}. Saldo wynosi: {work_with_context_manager.main_saldo}" 
                    work_with_context_manager.logs.append(log)
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
                    work_with_context_manager.main_saldo += price * current_amount
                    product.change_amount(-current_amount)
                    log = f"Stan magazynowy produktu {product.name} zmniejszono o liczbę {current_amount}. Saldo wynosi: {work_with_context_manager.main_saldo}." 
                    print(log)
                    work_with_context_manager.logs.append(log)
                    #parameters.extend([product_id, price, current_amount])

