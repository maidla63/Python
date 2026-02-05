def kuu_nimi(jarjekorranumber):
    kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", 
            "juuli", "august", "september", "oktoober", "november", "detsember"]
    return kuud[jarjekorranumber - 1]

def kuupaev_sonena(kuupaev):
    
    osad = kuupaev.split(".")
    paev = osad[0]
    kuu = int(osad[1])
    aasta = osad[2]
    
    kuu_tekst = kuu_nimi(kuu)
    
    return f"{paev}. {kuu_tekst} {aasta}. a"

kuupaev_kujul = input("Kirjuta kuupäev selles formaadis DD.MM.YYYY: ")

tulemus = kuupaev_sonena(kuupaev_kujul)
print(tulemus)