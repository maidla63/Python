import turtle
turtle.speed(0)
turtle.color("red")

suurus = 100
for i in range(10):
    turtle.lt(360/10)
    for i in range(3):
        turtle.fd(suurus)
        turtle.left(120)

turtle.done()
