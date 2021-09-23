import requests
import sys
from pprint import pprint

API_KEY = sys.argv[1]

def get_precipitation(date):

    url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

    querystring = {"q":"Lodz","days":"1","dt":f"{date}"}

    headers = {
        'x-rapidapi-host': "weatherapi-com.p.rapidapi.com",
        'x-rapidapi-key': API_KEY
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    #pprint(response.json())

    return response.json()["forecast"]['forecastday'][0]['day']["totalprecip_mm"]

#print(get_total_precipitation(sys.argv[2]))
