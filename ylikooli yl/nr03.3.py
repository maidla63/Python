fail = open("ylikooli yl/konto.txt", encoding="UTF-8")
for rida in fail:
    arv = float(rida)
    if arv > 0:
        print(arv)