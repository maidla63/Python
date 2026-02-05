
failinimi = input("Sisesta faili nimi: ")

tee = "ylikooli yl/" + failinimi

from datetime import *
paev = datetime.now().day
print(f"Tana on {paev}. kuupaev")

failinimi = "ylikooli yl/nimekiri.txt"
fail = open(failinimi, "r", encoding="utf-8")

nimed = []
for rida in fail:
    nimed.append(rida.strip())

fail.close()

arv_vastajaid = 1
print("Täna peavad vastama:")
for i in range(arv_vastajaid):
    koht = (paev + i) % len(nimed)
    print(f"{i + 1}. {nimed[koht]}")