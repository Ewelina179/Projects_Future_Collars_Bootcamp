import sys

from all_func import change_saldo

magazyn_dict = {}

file = sys.argv[1]
change_in_account = int(sys.argv[2])

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

new_saldo = str(change_saldo(change_in_account, saldo))

with open("warehouse.txt", "w") as fd:
    fd.write("saldo" + ";" + new_saldo + ";" +"\n")
    for key, value in magazyn_dict.items():
        x = str(key) + ";" + str(value['amount']) + ";" + str(value['price']) + "\n"
        fd.write(x)

print(new_saldo)
# zapisz to do pliku

# też zapisz (nie nadpisz) logi do pliku logi i paranetry do parametry
with open ("logs.txt", "a"):
    pass

with open ("parameters", "a"):
    pass



# sys.argv[3] - komentarz