import requests
from datetime import datetime
import sys
import os


class WeatherForecast:
    def __init__(self, api_key, date = str(datetime.today().date())): # chyba domyślnie następny dzień
        self.api_key = api_key
        self.date = date
        self.data = self.get_data(self.date)
        self.fp = open("weather.txt")
        self.info = self.get_from_file()

    def get_data(self, date):
        url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

        querystring = {"q":"Lodz","days":"1","dt":f"{date}"}

        headers = {
            'x-rapidapi-host': "weatherapi-com.p.rapidapi.com",
            'x-rapidapi-key': self.api_key
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
        return response.json()

    def get_rain_info(self):
        total_precipitation = float(self.data["forecast"]['forecastday'][0]['day']["totalprecip_mm"])
        return self.get_rain_chance(total_precipitation)

    def get_rain_chance(self, total_precipitation):
        if total_precipitation > 0:
            return "Będzie padać"
        elif total_precipitation <= 0:
            return "Nie będzie padać"
        else:
            pass


    def get_from_file(self):
        weathers = {}
        with open("weather.txt", "r") as f: # zmienić na filepath
            for line in f.readlines():
                splitted_line = line.split(";")
                weathers[splitted_line[0]] = splitted_line[1]
        return weathers

    def save_to_file(self, date, answer):
        with open('weather.txt', 'w') as f:
                f.write(str(date) + ";" + str(answer) + "\n")
                for key, value in self.info.items():
                    x = str(key) + ";" + str(value)
                    f.write(x)

    def check_is_valid(date):
        pass

    def __getitem__(self, key):
        try:
            return self.info[key]
        except:
                # self.check_is_valid_date
                self.data = self.get_data(key)
                self.save_to_file(key, self.get_rain_info())
                return self.get_rain_info()

    def items(self):
        for key, value in self.info.items(): # to ma być z tego cachowanego - 
            yield(key, value)

    def __iter__(self):
        for date in self.info.keys():
            yield(date)


# wf[date] da odpowiedź na temat pogody dla podanej daty (według specyfikacji z poprzedniego zadania)
# wf.items() zwróci generator tupli w formacie (data, pogoda) dla już zcache’owanych rezultatów przy wywołaniu
# wf to iterator zwracający wszystkie daty, dla których znana jest pogoda

wf = WeatherForecast(sys.argv[1])

print(wf["2021-10-15"])

for x in wf.items():
    print(x)

for x in wf:
    print(x)

print(wf.info)
print(wf["2021-10-10"])
print(wf.get_rain_info())