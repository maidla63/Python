# Ülessane 09
# Anri Maidla
# 15.12.2025
# Genereeri ja kuva arvud arvud 1-20
#for i in range(1,21):
 #       print(i, end=" ")
# Kasuta loendit 60, 5, 4, 42, 99, 67, 47, 22, 34, 8, 85, 50, 94, 39, 54, 83, 27, 40, 17, 75

print("\-----------------------")
loend = [60, 5, 4, 42, 99, 67, 47, 22, 34, 8, 85, 50, 94, 39, 54, 83, 27, 40, 17, 75]
for i in loend:
        print(i, end =" ")
paaris = []
paaritud = []
for i in loend:
        #print(i, end=" ")
        if i%2==0:
            paaris.append(i)
        else:
            paaritud.append(i)
print(f"paaris arvude summa on {sum(paaris)}")
print(f"paaritute arvude summa on {sum(paaritud)}")

# Leia kõik arvud vahemikus 200 kuni 320, mis jaguvad 7-ga, kuid ei jagu 5-ga. Prindi need arvud komadega eraldatult ühele reale.
for i in range(200,321):
    if i%7==0 and i%5 != 0:
        print(i, end=", ")
        
# Sulle on saadetud õpilaste keskmised hinded, mille lisasid loendisse. Eralda hinded ning leia kogu rühma parim ja kehvem tulemus ning keskmine hinne.
ryhma_hinded = ["Mari 4.9", "Jüri 3.1", "Kadri 4.6", "Marko 4.7", "Liis 4.9", "Andres 4.2", "Anu 4.7", "Martin 4.2", "Piret 4.2", "Tõnu 4.1"]
parim_tyyp= ""
parim_tyyp= 0
parim_keskmine = 0.
h_keskmine = 5.0
h_tyyp= ""
h_tyyp= 0
for i in ryhma_hinded:
    nimi, keskmine = i.split(" ")
    if float(keskmine) > parim_keskmine:
        parim_tyyp = nimi
        parm_keskmine= float(keskmine)
    elif float(keskmine) < h_keskmine:
        h_tyyp = nimi
        h_keskmine= float(keskmine)
        
print(parim_tyyp)
print(h_tyyp)