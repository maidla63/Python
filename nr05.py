# Ülessane 5
# 25.11.2025


# 5.1

# Sa oled loomas programmi, mis aitab kontrollida, kas inimesed vastavad vanusepiirangu nõuetele üritusel osalemiseks.
# Programm palub kasutajal sisestada oma vanuse. Kui vanus on vähemalt 18 aastat, siis programm annab teada, et kasutaja võib üritusele siseneda. Kui vanus on alla 18, siis programm teatab, et üritusele sisenemiseks ei ole piisavalt vana.
# Kasuta if ja else lauseid, et luua see vanusekontrolli programm.

piirang = 13 
vanus = int(input("Sisesta oma vanus:"))
if vanus >=piirang:
    print("Saab sisse")
else:
    print("Ei saa sisse")


# 5.2
import random
arv1 = random.randint(1,10)
arv2 = random.randint(1,10)
vastus = int(input(f"{arv1} * {arv2} =  "))
if vastus == arv1*arv2:
    print("Õige!")
else:
    print("nõrk")