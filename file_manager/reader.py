import sys
import os

from manager.file_manager_class import Manager

file = sys.argv[1]
file_to_write = sys.argv[2]
to_change = sys.argv[3:]

FORMATS = [".csv", ".json", ".pickle"]
# tu pobierze argumenty, wyłap wyjątki podczas odpalania argumentów i zaincjuj klasy
# i w sumie to wszędzie to samo. może getattr?

def change_file():
    z = [x for x in FORMATS if x == file_to_write[-4:]][0] # z to konkretna literka - c, j lub p
    if z:
        file_obj = Manager(c=True) # powinno zwrócić obiekt Csv_Manager-a
        file_obj.file = file
        file_obj.file_to_write = file_to_write
        file_obj.read_file()
        file_obj.show_file()
        file_obj.change_file(to_change)
        file_obj.save_to_file(to_change)

     # to wyżej - i jak pasuje to niech stworzy adekwatną instancję i odpali metody

try:
    pass 
# dodatkowy wyjątek do wyłapania - gdy zły format X,Y, wartość
except: # jaki rodzaj???
    print(f"File doesn't exist. List of files in current directory: {os.listdir(os.curdir)}")

change_file()