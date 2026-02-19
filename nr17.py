# # Sinu ülesandeks on kirjutada Pythoni skript, mis loeb andmeid failist pangakonto.txt. Fail sisaldab eraldi ridadel pangatehingute summasid: positiivsed summad tähistavad sissetulekuid ja negatiivsed summad väljaminekuid. Skript peab arvutama ja väljastama:
# kogu tehingute arvu
# positiivsete tehingute arvu
# positiivsete tehingute kogusumma
# Tulemused tuleb väljastada konsooli

tehingute_arv = 0
pos_tehingute_arv = 0
pos_tehingute_summa = 0


fail = open("tekstfailid/pangakonto.txt", encoding="UTF-8")
for rida in fail:
        tehingute_arv+=1
        if float (rida.strip()) > 0:
            pos_tehingute_arv+=1
            pos_tehingute_summa+=float(rida.strip())
            print(rida.strip())

print(f"Tehingute arv: {tehingute_arv}")
print(f"Positiivsed Tehingud: {pos_tehingute_arv}")
print(f"Tehingute summa: {pos_tehingute_summa}")