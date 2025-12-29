import turtle
turtle.speed(0)
turtle.color("blue")


suurus = 60
for i in range(5):
    turtle.left(360/5)
    for i in range(4):
        turtle.fd(suurus)
        turtle.left(90)

turtle.done()