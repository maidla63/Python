import os 
from datetime import date 
# Skript tervitab kasutajat tema operatsioonisüsteemi sisselogimisnime alusel
print("Tere!",os.getlogin())

# Skript kuvab kasutajale praeguse töökataloogi tee
print(os.getcwd)

# Skript küsib kasutajalt, mitu kataloogi ta soovib luua 

katalooginimi = int(input("Mitu kataloogi soovid: "))

# Kataloogid luuakse praegusesse töökataloogi kuupäevaga märgistatud kataloogi sees, nummerdatuna (nt “1”, “2”)#
today = str(date.today())
try:
    os.mkdir(today)
    for i in range(katalooginimi):
        os.mkdir(today+"/"+str(i+1))
except FileExistsError:
    print("Kataloog 'uus_kaust' juba eksisteerib.")

