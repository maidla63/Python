# Kordamine / Harjutamine
# Anri Maidla
# 09.12.2025

# Harjutus 1

tunnid=2
minutid=38
sekundid=59

aeg=f"{tunnid} {minutid} {sekundid} pm"
print(aeg)


# Harjutus 2

tsitaat="Parimad asjad maailmas ei ole asjad. - Jaagup Kreem"
print(tsitaat)

# Harjutus 03

eesnimi= "Jüri" 
perenimi= "Jurakas"
print(f"{eesnimi} {perenimi}, nimetähed on {eesnimi[0]} . {perenimi[0]}")


# Harjutus 05
kasutaja= "karrolk@gmail.com"

kasutaja= kasutaja.replace("@gmail.com", "@netlog.com")
print(kasutaja)

# Harjutus 07

sõidu_kaugus= 10
kiirus= 75

sõiduaeg=(sõidu_kaugus/kiirus)
print(sõiduaeg)
print(f"Sõiduaeg on {sõiduaeg} tundi")

# Harjutus 09

voimsus=400
hind=9.69

voolutarbimine=voimsus / 1000
tasu=voolutarbimine*hind
print(tasu)

# Harjutus 11
numbrid= "numbrid olid katki ja ma ei osand parandata"
x = numbrid.split()
otsitav= "35482977"
pool = int(len(x))/2
kokku = int(len(x))
try:
    print(len(x))
    print(x.index(otsitav))
    print(x[pool:kokku])
except:
    print("Numbrit pole!")

# Harjutus 13

t=10
if t > 25:
    print("Väga kuum on, ei tasu õue minna")
elif 25 <= t <= 25:
        print("Mõnus temperatuur")
else:
     print("kuradima jahe on")
     
# Harjutus 15

products= ["Õunad", "Piim", "Leib", "Juust", "Tomatid", "Kanafilee", "Muna", "Sibul",
"Apelsinid", "Riis", "Jogurt", "Kartul", "Kalafilee", "Pasta",
"Jogurtijook", "Porgandid", "Virsikud", "Pähklid", "Rosinad", "Kapsas",
"Kreeka jogurt", "Veiseliha", "Banaanid", "Oliivid", "Mandlid", "Maguskartul", "Greibid"];
nr = 1
for x in products:
    if x == "Muna":
        continue
    if x == "Sibul":
        continue
    if x == "Riis":
         continue   
    print(f"{nr}, {x}")
    nr +=1
    if nr ==11:
        break