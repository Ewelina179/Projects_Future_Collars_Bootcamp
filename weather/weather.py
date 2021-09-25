import sys
import requests
import datetime
from precip import get_precipitation
from pprint import pprint
from check_date import check_date

next_day = str(datetime.date.today() + datetime.timedelta(days=1))

weathers = []
with open("weather.txt", "r") as f:
        for line in f.readlines():
            splitted_line = line.split(";")
            data = splitted_line[0], splitted_line[1]
            weathers.append(data)
try:
    date = sys.argv[2]
except:
    date = next_day

tuple_date = tuple(map(int, date.split('-')))
check = check_date(tuple_date[0], tuple_date[1], tuple_date[2])

lst_of_dates = [x for x in weathers if date in x]

if check:
    if lst_of_dates:
        print(lst_of_dates[0][1])
    else:
        try:
            precipitation = get_precipitation(date)
            if precipitation > 0:
                answer = "Będzie padać"
            else:
                answer = "Nie będzie padać"
            with open('weather.txt', 'w') as f:
                f.write(str(date) + ";" + str(answer) + "\n")
                for el in weathers:
                    x = str(el[0]) + ";" + str(el[1])
                    f.write(x)
            print(answer)
        except:
            print("Nie wiem.") # kiedy dzień spoza dat dla których API ma pogodę
else:
    print("Niepoprawna data.") # zły format lub nie ma takiej w kalendarzu