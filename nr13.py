import turtle

t=turtle
screen = turtle.Screen()

t.speed(0)
# Teksti kuvamine
pikkus = screen.numinput("Pikkuse sisetamine", "Kui pikka on vaja", default=20, minval=0, maxval=100)
pikk = 10


number = 1 
for i in range(1, int(pikkus)): 
    t.lt(90)
    t.fd(20+pikk)
    t.write(number, font=("Arial", 12, "normal"))
    t.bk(20+pikk)
    t.rt(90)
    t.fd(20)
    if i%5==0:
        pikk = 10
    else:
        pikk = 0 
        number= " "
    number += i

t.done()