import requests

def load_airiq():
    endpoint = "https://api.airvisual.com/v2/city?city=Belgrade&state=central-serbia&country=serbia&key=a21a8af4-4e8e-4566-a53f-06abdbe4f254"
    r = requests.get(endpoint)    
    content = r.json()
    return content['data']['current']['pollution']['aqius']

def load_weather():
    endpoint = "https://api.openweathermap.org/data/2.5/weather?id=792680&appid=d7672273f293e18bae7860fce2a5feed"
    r = requests.get(endpoint)    
    content = r.json()
    temp = content['main']['temp'] - 273.15
    return round(temp)