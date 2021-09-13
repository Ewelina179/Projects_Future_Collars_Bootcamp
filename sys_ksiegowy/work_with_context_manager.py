import os.path
from my_context_manager import FileManager
from warehouse import main_warehouse, Product
from main import file

logs = []

if os.path.exists(file):
    with FileManager(file, "r") as fd:
        line = fd.readline()
        sline = line.split(";")
        main_saldo = float(sline[1])

    with FileManager(file, "r") as fd:
        for line in fd.readlines()[1:]:
            splitted_line = line.split(";")
            product = Product( name = splitted_line[0], amount = int(splitted_line[1]), price = float(splitted_line[2]))
            main_warehouse.add_product(product)

    with FileManager("logs.txt", "r") as fd:
        for line in fd.readlines():
            logs.append(line)
else:
    main_saldo = 0

with FileManager(file, "w") as fd:
        fd.write("saldo" + ";" + str(main_saldo) + ";" +"\n")
        for product in main_warehouse.products:
            x = str(product.name) + ";" + str(product.amount) + ";" + str(product.price) + "\n"
            fd.write(x)

with FileManager("logs.txt", "w") as fd:
    for el in logs:
        fd.write(el)