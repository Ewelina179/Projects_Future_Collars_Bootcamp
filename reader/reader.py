import sys
import os
import csv

file = sys.argv[1]
file_to_write = sys.argv[2]
to_change = sys.argv[3:]
lst = []
lst_to_change=[]

for el in to_change:
    b = el.split(",")
    c = [int(x) for x in b[:-1]]
    d = c[0], c[1], b[2]
    lst_to_change.append(d)

try:
    with open(file, newline="") as f:
        reader = csv.reader(f)
        for line in reader:
            lst.append(line)

    for el in lst_to_change:
        lst[el[0]][el[1]]= el[2]

    with open(file_to_write, 'w', newline="") as f: 
        csvwriter = csv.writer(f) 
        csvwriter.writerows(lst) 
        
except:
    print(f"Files in current directory: {os.listdir(os.curdir)}")
