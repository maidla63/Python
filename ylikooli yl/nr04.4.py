def tervitus(jarjekorranumber):
    print(f'Mario: "Tere!"')
    print(f"Tänа {jarjekorranumber}. kord suurelt ja soojalt tere õelda, mõtleb mario")
    print(f'Külaline: "Jah, See on AI"')

arv = int(input("Sisestage külaliste arv: "))

for i in range(1, arv + 1):
    tervitus(i)