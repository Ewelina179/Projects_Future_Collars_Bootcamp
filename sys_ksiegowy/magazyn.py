import sys

from my_context_manager import FileManager
from warehouse import Product, Warehouse, main_warehouse

from internal_part_of_program import get_command
import work_with_context_manager
from main import file

argument = sys.argv[0]

get_command(argument)

for el in sys.argv[2:]:
        product = [x for x in main_warehouse.products if x.name == el][0]
        if product:
            print(f"Stan magazynowy dla produktu {product.name} wynosi: {product.amount}.")
        else:
            print(f"Nie ma wskazanego produktu: {el}.")


with FileManager(file, "w") as fd:
    fd.write("saldo" + ";" + str(work_with_context_manager.main_saldo) + ";" +"\n")
    for product in main_warehouse.products:
            x = str(product.name) + ";" + str(product.amount) + ";" + str(product.price) + "\n"
            fd.write(x)

with FileManager("logs.txt", "w") as fd:
    for el in work_with_context_manager.logs:
        fd.write(el)

with FileManager("parameters", "a"):
    pass
