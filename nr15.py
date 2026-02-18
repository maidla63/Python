import turtle
import random

skoor = 0

aken = turtle.Screen()
aken.bgcolor("lightblue")
aken.setup(width=600, height=600)
aken.tracer(0)

# ristkülik
ristkylik = turtle.Turtle()
ristkylik.shape("square")
ristkylik.shapesize(stretch_wid=1, stretch_len=5)
ristkylik.penup()
ristkylik.color("black")
ristkylik.goto(0, -250)

# ring
ring = turtle.Turtle()
ring.shape("circle")
ring.penup()
ring.speed('fastest')
ring.goto(0, 0)
ring.setheading(random.randint(45, 135))

# skoori kuvamine
skoor_text = turtle.Turtle()
skoor_text.hideturtle()
skoor_text.penup()
skoor_text.goto(0, 260)
skoor_text.color("black")

def uuenda_skoor():
    skoor_text.clear()
    skoor_text.write(f"Skoor: {skoor}", align="center", font=("Arial", 20, "bold"))

uuenda_skoor()

# kiirused
ristkyliku_kiirus = 20
kiirus = 8
mang_kaib = True

# ristküliku funktsioonid
def liigu_vasakule():
    x = ristkylik.xcor()
    y = ristkylik.ycor()
    if x > -250:
        ristkylik.setx(x - ristkyliku_kiirus)

def liigu_paremale():
    x = ristkylik.xcor()
    if x < 250:
        ristkylik.setx(x + ristkyliku_kiirus)

# ringi funktsioonid
def peegelda_porkumisel():
    global skoor, kiirus, ristkyliku_kiirus, mang_kaib
    
    nurk = ring.heading()
    
    if ring.xcor() >= 290 or ring.xcor() <= -290:
        uus_nurk = 180 - nurk
        if uus_nurk < 0:
            uus_nurk += 360
        ring.setheading(uus_nurk)
    
    if ring.ycor() >= 290:
        uus_nurk = 360 - nurk
        ring.setheading(uus_nurk)
    
    if ring.ycor() <= -290:
        mang_kaib = False
        skoor_text.goto(0, 0)
        skoor_text.color("black")
        skoor_text.write(f"heh üle said!\n skoor: {skoor}", align="center", font=("Arial", 24, "bold"))
        return
    
    x = ristkylik.xcor()
    y = ristkylik.ycor()
    
    if (ring.ycor() - 10 <= y + 10 and ring.ycor() >= y - 10 and 
        ring.xcor() >= x - 50 and ring.xcor() <= x + 50):
        
        uus_nurk = 360 - nurk
        ring.setheading(uus_nurk)
        
        skoor += 1
        uuenda_skoor()
        
        if skoor % 5 == 0:
            kiirus += 1
            ring.color("red")
        else:
            ring.color("black")
        
        if skoor % 10 == 0:
            ristkyliku_kiirus += 5

def ring_liigu():
    global mang_kaib
    
    if not mang_kaib:
        return
    
    ring.forward(kiirus)
    peegelda_porkumisel()
    aken.update()
    aken.ontimer(ring_liigu, 20)

# klaviatuurile reageerimine
aken.listen()
aken.onkeypress(liigu_vasakule, "Left")
aken.onkeypress(liigu_paremale, "Right")

ring_liigu()

aken.mainloop()