import sys

saldo = 1500
store = {"produkt1": {"amount":2, "price": 12}, "produkt2": {"amount":2, "price": 12}, "produkt3": {"amount":2, "price": 12}, "produkt4": {"amount":2, "price": 12}}

list_of_logs = []
parameters = []

COMMANDS = "saldo", "sprzedaz", "zakup", "konto", "magazyn", "przeglad"

argument = sys.argv[1]

while argument in COMMANDS:

    commands2 = "saldo", "zakup", "sprzedaz", "stop"

    answer = input("Podaj komendę z dostepnych: ") 

    if answer not in commands2:
        print("Niewłaściwa komenda.")
        continue

    if answer == "stop":
        break

    elif answer == "saldo":
        change_in_account = float(input("Zmiana na koncie wyrażona w groszach: "))
        saldo += change_in_account*0.01
        comment = input("Komentarz do zmiany: ")
        log = f"Zmieniono wartość salda o {change_in_account * 0.01} złotych. Saldo po zmianie wynosiło {saldo}."
        list_of_logs.append(log)
        parameters.append(change_in_account)
        parameters.append(comment)
        
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
                if not store.get(product_id):
                    store[product_id] = {"amount":current_amount, "price": price}
                else:
                    amount = store[product_id]['amount']
                    store[product_id]={'amount': amount + current_amount} # chyba słownik powinien mieć inną konstrukcję. dwie ceny - po jakiej kupujemy i po jakiej sprzedajemy. w takiej formie tym punkcie chyba nie powinien zmieniać ceny.

                log = f"Stan magazynowy produktu {product_id} podniesiono o liczbę {current_amount}. Saldo wynosi: {saldo}" 
                list_of_logs.append(log)
                parameters.extend([product_id, price, current_amount]) # czy program ma zapisywać wszystkie parametry, czy tylko te, które miały wpływ na saldo? nie do końca rozumiem punkt V. właściwie wcale nie rozumiem.

    elif answer == "sprzedaz":
        product_id = input("Podaj identyfikator produktu: ")
        price = float(input("Podaj cenę jednostkową: "))
        current_amount = int(input("Podaj liczbę sztuk: "))

        if price < 0 or current_amount < 0:
            print("Liczba sprzedanych sztuk nie może być ujemna. Cena produktu nie może być ujemna.")
            continue # (wg założen z zadania powinno być break wszędzie)
        if not store.get(product_id):
            print(f"W magazynie nie ma takiego produktu: {product_id}")
            continue
        else:
            if store[product_id]['amount'] < current_amount:
                print("Brak wystarczającej liczby sztuk produktu.")
                continue
            else:
                saldo += price * current_amount
                amount = store[product_id]['amount']
                store[product_id]={'amount': amount - current_amount}
                log = f"Stan magazynowy produktu {product_id} zmniejszono o liczbę {current_amount}. Saldo wynosi: {saldo}." 
                list_of_logs.append(log)
                parameters.extend([product_id, price, current_amount])

if argument == "saldo":
    change_in_account = float(sys.argv[2])
    saldo += change_in_account*0.01
    comment = sys.argv[3]
    log = f"Zmieniono wartość salda o {change_in_account * 0.01} złotych. Saldo po zmianie wynosiło {saldo}."
    list_of_logs.append(log)
    parameters.extend([float(sys.argv[2]), sys.argv[3]])
    print(f"Podane podczas działania programu parametry: {parameters}.")

elif argument == "sprzedaz":
    product_id = sys.argv[2]
    price = float(sys.argv[3])
    current_amount = int(sys.argv[4])
    if price < 0 or current_amount < 0:
        print("Liczba sprzedanych sztuk nie może być ujemna. Cena produktu nie może być ujemna.")
    if not store.get(product_id):
        print(f"W magazynie nie ma takiego produktu: {product_id}")
    else:
        if store[product_id]['amount'] < current_amount:
            print("Brak wystarczającej liczby sztuk produktu.")
        else:
            saldo += price * current_amount
            amount = store[product_id]['amount']
            store[product_id]={'amount': amount - current_amount}
            log = f"Stan magazynowy produktu {product_id} zmniejszono o liczbę {current_amount}. Saldo wynosi: {saldo}." 
            list_of_logs.append(log)
            parameters.extend([sys.argv[2], float(sys.argv[3]), int(sys.argv[4])]) 
    print(f"Podane podczas działania programu parametry: {parameters}.")

elif argument == "zakup":
    product_id = sys.argv[2]
    price = float(sys.argv[3])
    current_amount = int(sys.argv[4])
    if price < 0 or current_amount < 0:
        print("Liczba sztuk nie może być mniejsza od 0. Cena nie może być ujemna.")
    else:
        total_price = price * current_amount
        if saldo < total_price:
            print("Saldo nie może być ujemne.")
        else:
            saldo -= total_price
            if not store.get(product_id):
                store[product_id] = {"amount":current_amount, "price": price}
            else:
                amount = store[product_id]['amount']
                store[product_id]={'amount': amount + current_amount} 
            log = f"Stan magazynowy produktu {product_id} podniesiono o liczbę {current_amount}. Saldo wynosi: {saldo}" 
            list_of_logs.append(log)
            parameters.extend([sys.argv[2], float(sys.argv[3]), int(sys.argv[4])]) 
    print(f"Podane podczas działania programu parametry: {parameters}.")
    
elif argument == "konto":
    print(f"Stan konta wynosi: {saldo}.")

elif argument == "magazyn":
    for el in sys.argv[2:]:
        x = store.get(el)
        if x:
            print(f"Stan magazynowy dla produktu {el} wynosi: {x['amount']}.")
        else:
            print(f"Nie ma wskazanego produktu: {el}.")

elif argument == "przeglad":
    pass # Program wypisuje wszystkie akcje zapisane pod indeksami w zakresie [od, do] (zakresy włącznie) - ale nie podano zakresu na start. nie rozumiem - na wejściu nie podajemy jaki zakres chcemy odczytać
    print(f"Lista akcji: {list_of_logs}.") # historia od najnowszych do najstarszych jest
else:
    print("Niepoprawna komenda. Spróbuj ponownie.")
