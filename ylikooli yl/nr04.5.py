def pronksikarva_summa(taisarvud):
    summa = 0
    for arv in taisarvud:
        if arv == 1 or arv == 2 or arv == 5:
            summa += arv
    return summa

failinimi = input("Sisesta failinimi: ")

tee = "ylikooli yl/" + failinimi

fail = open(tee, "r", encoding="utf-8")

taisarvud = []
for rida in fail:
    arv = int(rida.strip())
    taisarvud.append(arv)

fail.close()

tulemus = pronksikarva_summa(taisarvud)

print(f"Hoiupõrsaasse läheb {tulemus} senti.")