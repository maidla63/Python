# Ülessane 19
# 06.03.2026

# Kuva 12.klassi õpilaste nimekiri
# Kuva mitu õpilast õpib 10, 11 ja 12 klassis
# Kuva millistes trennides 12. klassi õpilased käivad
# Kuva 12 klassi õpilaste hinneteleht (nimi, ained, punktid)


import json

with open('tekstfailid/haridustulemused.json', 'r', encoding='utf-8') as file:
    tulemused = json.load(file)

klass12 = 0
klass11 = 0
klass10 = 0
tegevused = []



for tulem in tulemused:
# Kuva 12.klassi õpilaste nimekiri
    if tulem['klass'] =="12":
        for aine,hinne in tulem['hinded'].items():
            print("\t",aine, hinne)
        print(tulem['nimi'])
        klass12 +=1
        for tegevus in (tulem['tegevused']):
            if tegevus not in tegevused:
                tegevused.append(tegevus)
    elif tulem['klass'] == "11":
        klass11 +=1
    else:
        klass10 +=1

print(f"12. Klassis õpib {klass12} õpilast")
print(f"11. Klassis õpib {klass11} õpilast")
print(f"10. Klassis õpib {klass10} õpilast")
for i in tegevused:
    print(i, end= ", ")