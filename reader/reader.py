import sys
import csv


file = sys.argv[1]
file_to_write = sys.argv[2]
lst = []
to_change = sys.argv[3:]

n=[]
for el in to_change:
    b = el.split(",")
    c = [int(x) for x in b[:-1]]
    d = c[0], c[1], b[2]
    n.append(d)
print(n)


# reader.py <src> <dst> <change1> <change2> ...


with open(file, newline="") as f:
	reader = csv.reader(f)
	for line in reader:
		lst.append(line)
print(lst)


for el in n:
    lst[el[0]][el[1]]= el[2]

print(lst)

with open(file_to_write, 'w', newline="") as f: 
    csvwriter = csv.writer(f) 
    csvwriter.writerows(lst)

