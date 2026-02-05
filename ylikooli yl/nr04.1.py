def banner(tekst):
    return tekst.upper()

reklaam = input("Sisesta reklaamtekst: ")

kordused = int(input("Mitu korda kuvada: "))

for i in range(kordused):
    print(banner(reklaam))