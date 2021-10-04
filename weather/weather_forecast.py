import requests
import datetime
import sys
import os

class WeatherForecast:
    def __init__(self, api_key):
        self.api_key = api_key
        self.date = str(datetime.date.today() + datetime.timedelta(days=1))
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

    def get_data_from_api(self, key):
        self.data = self.get_data(key)
        if self.get_rain_info():
            self.save_to_file(key, self.get_rain_info())
        return self.get_rain_info()

    def get_rain_info(self):
        try:
            total_precipitation = float(self.data["forecast"]['forecastday'][0]['day']["totalprecip_mm"])
            return self.get_rain_chance(total_precipitation)
        except IndexError:
            print("Dane na temat pogody obecnie niedostępne.")

    def get_rain_chance(self, total_precipitation):
        if total_precipitation > 0:
            return "Będzie padać"
        elif total_precipitation <= 0:
            return "Nie będzie padać"

    def get_from_file(self):
        weathers = {}
        with open("weather.txt", "r") as f:
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

    def get_data_from(self, key):
        if self.info.get(key):
            return self.info[key]
        return self.get_data_from_api(key)

    def __getitem__(self, key):
        return self.get_data_from(key)
    
    def items(self):
        for key, value in self.info.items():
            yield(key, value)

    def __iter__(self):
        return iter(self.info.keys())

wf = WeatherForecast(sys.argv[1])

print(wf["2021-10-10"])

for x in wf.items():
    print(x)

for x in wf:
    print(x)
