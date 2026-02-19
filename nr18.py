

    # Korvpalli Tulemused
# Kuva mitu meeskonda osales ja too välja nimekiri (täpitähed peavad korras olema ja jälgi, et esimese rea jätad vahele)
# Leia mitu mängu igal meeskonnal oli (kasuta sõnastikku, kui meeskond on juba sõnastikus, siis suurendad selle väärtust +1)
# Leia iga meeskonna võidud ja kaotused ning kirjuta tulemused uude Exceli sõbralikku CSV faili

import csv

faili_nimi = 'tekstfailid/EstonianBasketballGames.csv'

meeskonnad = {}

with open(faili_nimi, mode='r', encoding='utf-8') as fail:
    csv_lugeja = csv.reader(fail)

    pais = next(csv_lugeja)

    # print(f"Päise veerud: {pais}")
    for rida in csv_lugeja:
        if rida[1] not in  meeskonnad:
            meeskonnad.append(rida[1])
        if rida[2] not in  meeskonnad:
            meeskonnad.append(rida[2])
        # print(rida[2])

print (f"Meeskonnad kokku: {len(meeskonnad)}")