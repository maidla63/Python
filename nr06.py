# Ülessane 6
# 03.12.2025
# Anri Maidla


import math
import turtle

mootkava = 50
turtle.speed(0)

nurk = math.radians(53)
korgus = 4.4

kaugus = korgus / math.tan(nurk)
pikkus = round(math.sqrt(math.pow(korgus, 2) + math.pow(kaugus,2)))

print(pikkus)
print(kaugus)
print(nurk)
turtle.fd(kaugus * mootkava)
turtle.lt(90)
turtle.fd(korgus * mootkava)
turtle.lt(143)
turtle.fd(pikkus * mootkava)
print(pikkus)
