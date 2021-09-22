import sys
import requests
import datetime

API_KEY = sys.argv[1]
# może być stała lokalizacja
print(API_KEY)

current_date = datetime.datetime.today()
print(current_date)
next_day = current_date + datetime.timedelta(days=1)
print(next_day)

try:
    print(sys.argv[2])
except:
    date = next_day
    print(date)


response = requests.get('http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={API_KEY}')
print(response)

# wyżej odczytaj weather.txt. sprawdź, czy jest ta data. jeśli jest, wyprintuj wynik dla tej daty. inaczej odczytaj z api. jeśli odczytujesz z api, dopisz do pliku txt
with open('weather.txt', 'w') as f:
    pass