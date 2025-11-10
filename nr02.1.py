import turtle
t = turtle.Turtle()
aken = turtle.Screen()
aken.title("Sinilill - Anri") 
aken.setup(500,500)
t.speed(0) # K iirus 0 - 0 Animatsiooni. 
t.pensize(10)


# vars
t.penup()
t.goto(0,-200)
t.pendown()
t.pencolor("green")
t.lt(90)
t.fd(200)

# õis
t.pencolor("blue")
t.right(90)
t.circle(60)
t.begin_fill()
t.color("blue", "lightblue")
t.circle(60)
t.end_fill()

# emakas
t.penup()
t.goto(0,50)
t.pendown()
t.color("yellow")
t.pensize(20)
t.circle(10)
# leht

turtle.done()