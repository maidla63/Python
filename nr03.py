# Anri Maidla
# 18.11.2025
# Ülessane 3.1

# Loo muutuja nimi, mis sisaldab kasutaja nime (string)
# Loo muutuja vanus, mis sisaldab kasutaja vanust (integer)
# Loo muutuja keskmine_hinne, mis sisaldab kasutaja keskmist hinnet (float)
# Trüki välja lause, mis ühendab kõik kolm muutujat, nt: “Karin , 18 aastat vana ja keskmine hinne on 4.7”

nimi = "Anri"
vanus = 16
keskmine_hinne = 5.0

print(nimi, vanus, "aastat vana ja keskmine hinne on", keskmine_hinne)

# Ülessane 3.2
# Loo muutuja toode, mis sisaldab toote nime (string)
# Loo muutuja kogus, mis näitab, mitu toodet soovitakse osta (integer)
# Loo muutuja hind, mis näitab ühe toote hinda (float)
# Trüki välja lause, mis ühendab need andmed, nt: “Soovin porgandeid 3, mille tüki hind on 5.35 eurot.”
# Kasuta väljatrükkimisel ainult plussi (+)

toode= "Porgandeid"
kogus= 2
hind= 0.75
print("Soovin "+toode, kogus, "mille tüki hind on ", hind, "eurot")

# Ülessane 3.3
# Loo muutuja sihtkoht, mis sisaldab reisi sihtkohta (string)
# Loo muutuja paevade_arv, mis näitab, mitu päeva reis kestab (integer)
# Loo muutuja oobimise_hind, mis näitab ühe öö hinna (float)
# Trüki välja lause, mis ühendab need andmed, nt: “Soome reis kestab 5 päeva ja üks öö maksab 30.50 eurot.”

sihtkoht= "Soome"
paevade_arv= 5
oobimise_hind= 30.50
print(sihtkoht, "Reis kestab", paevade_arv, "paeva ja üks öö maksab", oobimise_hind, "eurot")

# Ülessane 3.6
# Loo muutuja kylje_pikkus, mis määrab kujundi külje pikkuse (täisarv)
# Loo muutuja nurk, mis määrab kujundi nurga (täisarv)
# Loo muutuja kujundi_varv, mis määrab kujundi joonevärvi (string)
# Kasutades Turtle’i, joonista kõrvuti 3 värvilist ruutu, mis kasutab loodud muutujaid
# Iga ruut on järgmisest 1,5 korda eemal
# Testi: muuda külje pikkust ning ruudud on kenasti teineteisest eemal

import turtle
kylje_pikkus = 100
nurk = 90
kujundi_varv = "purple"
kogus = 3
nihe = 1.5
turtle.speed(0)
turtle.color(kujundi_varv)

for j in range(kogus):
        for i in range (4):
            turtle.fd(kylje_pikkus)
            turtle.lt(nurk)
        turtle.penup()
        turtle.fd(kylje_pikkus*nihe)
        turtle.pendown()

turtle.done()