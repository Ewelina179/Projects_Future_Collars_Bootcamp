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
    print("Liczba sztuk nie może być mniejsza od 0. Cena nie może być ujemna.")
else:
    total_price = price * current_amount
    if work_with_context_manager.main_saldo < total_price:
        print("Saldo nie może być ujemne.")
    else:
        work_with_context_manager.main_saldo -= total_price
        if product_id not in work_with_context_manager.main_warehouse.lst_of_product_names():
            product = (product_id, current_amount, price)
            work_with_context_manager.main_warehouse.add_product(product)
        else:
            product = [x for x in main_warehouse.products if x.name == product_id][0]
            product.change_amount(current_amount)
        log = f"Stan magazynowy produktu {product_id} podniesiono o liczbę {current_amount}. Saldo wynosi: {work_with_context_manager.main_saldo}" 
        print(log)
        work_with_context_manager.logs.append(log)
        #parameters.extend([product_id, price, current_amount])
with open("warehouse.txt", "w") as fd:
    fd.write("saldo" + ";" + str(work_with_context_manager.main_saldo) +"\n")
    for product in main_warehouse.products:
            x = str(product.name) + ";" + str(product.amount) + ";" + str(product.price) + "\n"
            fd.write(x)

with open("logs.txt", "a") as fd:
    for el in work_with_context_manager.logs:
        fd.write(el)
