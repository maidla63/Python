import turtle

t=turtle
screen = turtle.Screen()

t.speed(0)
# Teksti kuvamine
pikkus = screen.numinput("Pikkuse sisetamine", "Kui pikka on vaja", default=20, minval=0, maxval=100)
pikk = 10


number = 0
for i in range(1, int(pikkus)): 
    t.lt(90)
    t.fd(10+pikk)
    t.bk(10+pikk)
    t.rt(90)
    t.fd(20)
    if i%5==0:
        pikk = 10
    else:
        pikk = 0 
       # number= "  "
    # number += i
    
t.goto(0,0)
t.lt(90)
t.fd(10+pikk+20)
t.rt(90)
t.penup()
for i in range(1, int(pikkus)): 
        if number%5==0:
            t.write(number, font=("Arial", 8, "normal"))
        t.fd(20)
        number+=1











t.hideturtle
t.done()