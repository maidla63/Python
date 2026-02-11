import turtle
ekraan = turtle.Screen()
# ekraan.numinput("Vali Kujund", "1 - Ruut 2 - Ring", default=1, minval=0, maxval=2)

def muuda_punane():
    turtle.color("red")
def muuda_roheline():
    turtle.color("green")
def muuda_sinine():
    turtle.color("blue")

ekraan.onkey(muuda_punane, "r")
ekraan.onkey(muuda_roheline, "g")
ekraan.onkey(muuda_sinine, "b")


def ruut(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.speed(0)
    for _ in range(4):
            turtle.fd(100)
            turtle.lt(90)


def vasakKlikk(x, y):
    for _ in range(8):
         turtle.undo()

ekraan.onscreenclick(ruut, 1) # Parem
ekraan.onscreenclick(vasakKlikk, 3) # Vasak klõps

ekraan.listen()

turtle.mainloop()