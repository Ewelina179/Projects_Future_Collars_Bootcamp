import sys
import requests
import datetime
from precip import get_total_precipitation
from pprint import pprint

current_date = datetime.datetime.today()
#print(current_date)
next_day = current_date + datetime.timedelta(days=1)
#print(next_day)


weathers = []
with open("weather.txt", "r") as f:
        for line in f.readlines():
            splitted_line = line.split(";")
            data = splitted_line[0], splitted_line[1]
            weathers.append(data)
try:
    date = sys.argv[2]
    #print(date)
except:
    date = next_day # ten poqoduje, że jak zły dzień podam to bierze kolejny dzień???
    #print(date)

print(weathers)

lst = [x for x in weathers if date in x]
print(lst)
precipitation = get_total_precipitation(date)
print(precipitation)
if lst:
    print(lst[0][1])
# tu jest "\n"
elif precipitation:
    if precipitation > 0:
        answer = "Będzie padać"
    else:
        answer = "Nie będzie padać"
    with open('weather.txt', 'w') as f:
        f.write(str(date) + ";" + str(answer) + "\n")
        for el in weathers:
            x = str(el[0]) + ";" + str(el[1])
            f.write(x)
    print(precipitation)
    print(answer)
else:
    print("Nie wiem.")