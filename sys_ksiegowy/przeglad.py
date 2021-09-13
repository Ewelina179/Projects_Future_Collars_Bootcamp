import sys

from my_context_manager import FileManager
from warehouse import Product, Warehouse, main_warehouse

from internal_part_of_program import get_command
import work_with_context_manager
from main import file

argument = sys.argv[0]

get_command(argument)

print(f"Lista logów: {work_with_context_manager.logs}")

with open ("parameters", "a"):
    pass
