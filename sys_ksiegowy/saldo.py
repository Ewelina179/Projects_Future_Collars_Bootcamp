import sys

from my_context_manager import FileManager
from warehouse import Product, Warehouse, main_warehouse

from internal_part_of_program import get_command
import work_with_context_manager
from main import file

change_in_account = int(sys.argv[2])

argument = sys.argv[0]

def change_saldo(change_in_account, saldo):
    saldo += change_in_account*0.01
    return saldo

get_command(argument)

if change_in_account < 0 and abs(change_in_account) > work_with_context_manager.main_saldo:
    print("Zmiana (ujemna) przekracza wartość salda. Nie można wykonać operacji.")
else:
    new_saldo = str(change_saldo(change_in_account, work_with_context_manager.main_saldo))
    log = f"Zmieniono wartość salda o {change_in_account * 0.01} złotych. Saldo po zmianie wynosiło {new_saldo}."
    print(log)
    work_with_context_manager.logs.append(log)
    with FileManager("warehouse.txt", "w") as fd:
        fd.write("saldo" + ";" + new_saldo + ";" +"\n")
        for product in main_warehouse.products:
            x = str(product.name) + ";" + str(product.amount) + ";" + str(product.price) + "\n"
            fd.write(x)
    with FileManager("logs.txt", "w") as fd:
        for el in work_with_context_manager.logs:
            fd.write(el) # z trybem "a" za każdym razem czytało cały plik i w tym momencie go dopisywało. stąd taki rozmiar pliku.

with open ("parameters", "a"):
    pass
