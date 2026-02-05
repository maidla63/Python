def mahlapakkide_arv(ounte_kogus):
    arv = ounte_kogus * 0.4 / 3
    return round(arv)

ounte_kogus = float(input("sisesta üks suur paks õuna kogus "))

mahlapakkide = mahlapakkide_arv(ounte_kogus)

print(mahlapakkide)