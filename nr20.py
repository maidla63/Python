# Loo Pythoni programm, mis küsib kasutajalt linnanime ja kasutades OpenWeatherMap API-d, kuvab vastava linna hetketemperatuuri Celsius kraadides
# Programm peab sisaldama vigade käsitlemist, näiteks kui linn ei ole leitav, päringule pole vastust ja kui API võti on vale
# Veendu, et programm suudab käidelda ka sisestatud linnanimede erinevaid kirjapilte

import requests

# API võtme ja linna nime määramine
city = input("Lisa otsitav asukoht ")
city = city.strip().capitalize()
print("Otsitav Linn", city)
api_key = "c188c3e92658fdb39455a4ede54feb3f"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# API päringu tegemine
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = data['main']['temp']
    print(f"Temperatuur: {temperature} °C")
else:
     print("Viga andmete allalaadimisel:", response.status_code)