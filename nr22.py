
from datetime import datetime, date

# # 1
# kp = datetime.datetime.now()
# print(kp)

# print(kp.strftime("%d.%m %Y, %H:%M:%S"))

# sp = datetime.datetime(2009,2,18)
# vanus_paevades = kp - sp
# print(f"Päevad: {vanus_paevades}")

# vanus_aastates = vanus_paevades.days // 365
# print(f"Aastad: {vanus_aastates}")

# if vanus_aastates%5==0:
#     print("Sul on juubel!")
# else:
#     print("Ära juubelda ront")


import csv
faili_nimi = 'tekstfailid/rentals.csv'
meeskonnad = {}

with open(faili_nimi, mode='r', encoding='utf-8') as fail:
    csv_lugeja = csv.reader(fail)

    pais = next(csv_lugeja)

