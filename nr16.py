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

kustuta = int(input("Milist kataloogi kustutada 1- {mitu}: "))

if os.path.isdir(f"{today}/{kustuta}"):
    os.rmdir(f"{today}/{kustuta}")
else:
    print(f"Selline kataloog puudub: {today}/{kustuta}")
              