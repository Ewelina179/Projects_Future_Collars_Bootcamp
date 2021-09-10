import sys

from all_func import change_saldo

magazyn_dict = {}

file = sys.argv[1]
product_id = sys.argv[2]
price = float(sys.argv[3])
current_amount = int(sys.argv[4])

with open(file, "r") as fd:
    line = fd.readline()
    sline = line.split(";")
    saldo = float(sline[1])

with open(file, "r") as fd:
    for line in fd.readlines()[1:]: # line to ciąg znaków - jeden element listy
        splitted_line = line.split(";") # rozbijam ciąg znaków (jedną line) - split - tam gdzie średnik był - wynikiem lista odrębnych słów

        product = splitted_line[0]
        product_amount = float(splitted_line[1])
        product_price = float(splitted_line[2])
        magazyn_dict[product] = {'amount':product_amount, 'price': product_price}

if price < 0 or current_amount < 0:
        print("Liczba sprzedanych sztuk nie może być ujemna. Cena produktu nie może być ujemna.")
if not magazyn_dict.get(product_id):
    print(f"W magazynie nie ma takiego produktu: {product_id}")
else:
    if magazyn_dict[product_id]['amount'] < current_amount:
        print("Brak wystarczającej liczby sztuk produktu.")
    else:
        saldo += price * current_amount
        amount = magazyn_dict[product_id]['amount']
        magazyn_dict[product_id]={'amount': amount - current_amount, 'price': price}
        log = f"Stan magazynowy produktu {product_id} zmniejszono o liczbę {current_amount}. Saldo wynosi: {saldo}." 
        print(log)
        #list_of_logs.append(log)
        #parameters.extend([sys.argv[2], float(sys.argv[3]), int(sys.argv[4])]) 
    #print(f"Podane podczas działania programu parametry: {parameters}.")

with open("warehouse.txt", "w") as fd:
    fd.write("saldo" + ";" + str(saldo) +"\n")
    for key, value in magazyn_dict.items():
        x = str(key) + ";" + str(value['amount']) + ";" + str(value['price']) + "\n"
        fd.write(x)

# dodać logi??? i parametry do jakiegoś pliku?