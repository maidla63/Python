ring = 6
porgandid = 0

for i in range(ring):
    r = i+1
    if r % 2 == 0:
        porgandid = porgandid + r
print(porgandid)