# Ülessane 09
# Anri Maidla
# 15.12.2025
# Genereeri ja kuva arvud arvud 1-20
#for i in range(1,21):
 #       print(i, end=" ")
# Kasuta loendit 60, 5, 4, 42, 99, 67, 47, 22, 34, 8, 85, 50, 94, 39, 54, 83, 27, 40, 17, 75

# print("\-----------------------")
# loend = [60, 5, 4, 42, 99, 67, 47, 22, 34, 8, 85, 50, 94, 39, 54, 83, 27, 40, 17, 75]
# for i in loend:
#         print(i, end =" ")
# paaris = []
# paaritud = []
# for i in loend:
#         #print(i, end=" ")
#         if i%2==0:
#             paaris.append(i)
#         else:
#             paaritud.append(i)
# print(f"paaris arvude summa on {sum(paaris)}")
# print(f"paaritute arvude summa on {sum(paaritud)}")

# Leia kõik arvud vahemikus 200 kuni 320, mis jaguvad 7-ga, kuid ei jagu 5-ga. Prindi need arvud komadega eraldatult ühele reale.
# for i in range(200,321):
#     if i%7==0 and i%5 != 0:
#         print(i, end=", ")
        
# Sulle on saadetud õpilaste keskmised hinded, mille lisasid loendisse. Eralda hinded ning leia kogu rühma parim ja kehvem tulemus ning keskmine hinne.
# ryhma_hinded = ["Mari 4.9", "Jüri 3.1", "Kadri 4.6", "Marko 4.7", "Liis 4.9", "Andres 4.2", "Anu 4.7", "Martin 4.2", "Piret 4.2", "Tõnu 4.1"]
# parim_tyyp= ""
# parim_tyyp= 0
# parim_keskmine = 0.
# h_keskmine = 5.0
# h_tyyp= ""
# h_tyyp= 0
# for i in ryhma_hinded:
#     nimi, keskmine = i.split(" ")
#     if float(keskmine) > parim_keskmine:
#         parim_tyyp = nimi
#         parm_keskmine= float(keskmine)
#     elif float(keskmine) < h_keskmine:
#         h_tyyp = nimi
#         h_keskmine= float(keskmine)
        
# print(parim_tyyp)
# print(h_tyyp)

# Koosta programm, mis genereerib ja kuvab korrutustabeli, kus iga number korrutatakse iseendaga:
# Näiteks:
# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# # 10 x 10 = 100


# for i in range(11): 
#     print(f"{i} * {1} = {i*i}")

# Loo programm, mis loob suvalised tehted 1-100 arvudega
# tehe = ["+","-","*","/"]
# import random
# for _ in range(10):
#     arv1 = random.randint(1,10)
#     arv2 = random.randint(1,10)
#     t = random.choice(tehe)
# if t=="+":
#     print(f"{arv1}{t}{arv2}={arv1 + arv2}")
# elif t=="-":
#     print(f"{arv1}{t}{arv2}={arv1 - arv2}")
# elif t=="*":
#     print(f"{arv1}{t}{arv2}={arv1 * arv2}")
# elif t=="/":
#     print(f"{arv1}{t}{arv2}={arv1 / arv2}")

# Täienda eelmist ülesannet ja kasutaja käest küsitakse vastust 

# tehe = ["+","-","*","/"]
# punktid = 0
# kysimuste_arv = 10
# import random
# for _ in range(10):
#     arv1 = random.randint(1,10)
#     arv2 = random.randint(1,10)
#     t = random.choice(tehe)
# if t=="+":
#     print(f"{arv1}{t}{arv2}=")
#     v = int(input("Vastus?"))
#     if arv1+arv2 == v:
#         print("Vastasid õigesti, aeg tobipausile.")
#         punktid+=1
# elif t=="-":
#     print(f"{arv1}{t}{arv2}=")
#     v = int(input("Vastus: "))
#     if arv1-arv2 == v:
#         punktid=1
# elif t=="*":
#     print(f"{arv1}{t}{arv2}=")
#     v = int(input("Vastus: "))
#     if arv1*arv2 == v:
#     else:
#         print(f"{arv1}{t}{arv2}=")
#         v = float(input("Vastus: "))
#         if round(arv1/arv2,1) == v:
#             punktid+=1
# print(f"{kysimuste_arv} - {punktid} - {punktid/kysimuste_arv}")
# if punktid/kysimuste_arv>= 0.5:
#     print("A")
# else:
#     print("MA")
# print(punktid)

# Kuva samasugused kujundid:
# 1
# arv = 5

# for i in range(1,6):
# print(" "*i,+"*" * arv)
# arv-=1

# 2
# arv = 5

# for i in range(1,6):
#     print("*" * arv)
#     arv = -1

# 3 
# arv = 5
# for i in range(1,6):
#     print(" " * arv + "*"*i)
#     arv = -1

# 4
# arv = 5
# for i in range(1,6):
# print("*" * i)
