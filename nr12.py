# Harjutus 12
# Anri Maidla 10.02.2026

# 12.1 

# def temp(t,v ):
#     """
#     Arvuta kahe arvu summa.

#     Parameetrid:
#     t (int): Kraadid.
#     v (String): vali teisendus F voi c .

#     Tagastab:
#     string: tagastab teisenduse või vea teate.

#     Näide:
#     >>> print(temp(20,"F"))
#     68
#     """
#     if v=="F":
#        vastus = t * 9/5 + 32
#     elif v=="C":
#         vastus = (t - 32) / (9/5)
#     else:
#         vastus = "Vale sisestus!"
#     return vastus
    

# print(temp(20,"F"))
# print(temp(79,"F"))
# print(temp(10,"C"))
# print(temp(70,"C"))
# print(temp.__doc__)

# 12.2
#10L/100 200km (200/100*10)
# kytus = lambda kulu, vahemaa: (vahemaa/100) * kulu

# print(kytus(10,200))

# 12.3

konto = 500

def depo(raha, konto):
    summa = konto + raha
    return summa

    """
     lahe funktsioon
    """

def valja(raha, konto):
    summa = konto - raha
    return summa

    """
     lahe funktsioon
    """

konto = depo(12, konto)
konto = depo(67, konto)
konto = valja(1, konto)
konto = depo(69, konto)
konto = depo(420, konto)

print("Kontoseis: ", konto)