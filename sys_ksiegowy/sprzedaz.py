import sys

from my_context_manager import FileManager
from warehouse import Product, Warehouse, main_warehouse

from internal_part_of_program import get_command
import work_with_context_manager
from main import file

product_id = sys.argv[2]
price = float(sys.argv[3])
current_amount = int(sys.argv[4])


argument = sys.argv[0]

get_command(argument)

if price < 0 or current_amount < 0:
        print("Liczba sprzedanych sztuk nie może być ujemna. Cena produktu nie może być ujemna.")
if product_id not in main_warehouse.lst_of_product_names():
    print(f"W magazynie nie ma takiego produktu: {product_id}")
else:
    product = [x for x in main_warehouse.products if x.name == product_id][0]
    if product.amount < current_amount:
        print("Brak wystarczającej liczby sztuk produktu.")
    else:
        work_with_context_manager.main_saldo += price * current_amount
        product.change_amount(-current_amount)
        log = f"Stan magazynowy produktu {product.name} zmniejszono o liczbę {current_amount}. Saldo wynosi: {work_with_context_manager.main_saldo}." 
        print(log)
        work_with_context_manager.logs.append(log)
        #parameters.extend([sys.argv[2], float(sys.argv[3]), int(sys.argv[4])]) 
    #print(f"Podane podczas działania programu parametry: {parameters}.")

with FileManager(file, "w") as fd:
    fd.write("saldo" + ";" + str(work_with_context_manager.main_saldo) +"\n")
    for product in main_warehouse.products:
            x = str(product.name) + ";" + str(product.amount) + ";" + str(product.price) + "\n"
            fd.write(x)

with FileManager("logs.txt", "w") as fd:
    for el in work_with_context_manager.logs:
        fd.write(el)
