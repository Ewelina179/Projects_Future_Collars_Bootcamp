import sys
import os

from manager.file_manager import Manager
file = sys.argv[1]
file_to_write = sys.argv[2]
to_change = sys.argv[3:]
path = os.path.dirname(os.path.abspath(__file__))

def get_file_type(file):
    return file.split(".")[-1]

f = get_file_type(file)

x = Manager(file, file_to_write, path, to_change, format=f)
print(f"Ścieżka pliku do odczytu {x.get_filepath()}")
print(f"Typ pliku, który ma zostać zmieniony {x.filetype}")
print(f"Plik zapisany w nowej lokalizacji (po zmianie): {x.changed_file}")