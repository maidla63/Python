import turtle
t = turtle.Turtle()
aken = turtle.Screen()
aken.title("Olümpiarõngad - Anri") 
aken.setup(500,400)
t.speed(0) # K iirus 0 - 0 Animatsiooni. 
t.pensize(6)
t.penup()
t.goto(-110,0)
t.pendown()
t.pencolor("blue")
t.circle(50)

t.pensize(6)
t.penup()
t.goto(0,0)
t.pendown()
t.pencolor("black")
t.circle(50)

t.pensize(6)
t.penup()
t.goto(110,0)
t.pendown()
t.pencolor("red")
t.circle(50)

t.pensize(6)
t.penup()
t.goto(-50,-50)
t.pendown()
t.pencolor("yellow")
t.circle(50)

t.pensize(6)
t.penup()
t.goto(55,-50)
t.pendown()
t.pencolor("green")
t.circle(50)



turtle.done()
