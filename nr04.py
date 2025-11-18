# Anri Maidla
# 18.11.2025
# Ülessane 4

# 1. Aia pikkus
# Kirjuta programm, mis aitab aiapidajal arvutada aia ümbermõõtu.
# Aed on ristküliku kujuline.
# Programm peaks küsima kasutajalt kahe aiaosa pikkused meetrites ja seejärel arvutama aia kogupikkuse.
# Väljasta lause, kasutades f-string vormindamist.
# Näide:
# Kasutaja sisestab: 4 ja 5
# Programm väljastab: Aia kogupikkus on 18 meetrit.


a= int(input("Anna kulg 1: "))
b= int(input("Anna kulg 2: "))
ymber= 2 * (a+b)

print(f"Aia kogupikkus on {ymber} meetrit.")

# 3. Faili allalaadimine
# Kirjuta programm, mis aitab arvutada, kui kaua kulub aega faili allalaadimiseks.
# Programm küsib kasutajalt faili suurust megabaitides (MB) ja allalaadimiskiirust megabaitides sekundis (MB/s).
# Seejärel arvutab programm allalaadimiseks kuluvat aega minutites.
# Lisa kontroll, et programm ei jookseks kokku, kui kasutaja sisestab ebakorrektse allalaadimiskiiruse (nt null või negatiivne arv).
# Väljasta lause, kasutades f-string vormindamist
# Näide:
# Kasutaja sisestab: faili suurus 500 MB, kiirus 20 MB/s
# Programm väljastab: Allalaadimiseks kulub 25 sekundit.
# Kui kasutaja sisestab kiiruseks 0 või teksti, siis programm ütleb: Tegid sisestamisel vea!

try:
    a=int(input("Anna faili suurus megabaitides: "))
    b= int(input("Anna Interneti kiirus megabait sekundites: "))
    aeg =  (a / b) / 60
    print(f"Allalaadimiseks kulub {aeg:0.20} minutit.")
except:
    print("lammas oled, kontrolli sisestust!")