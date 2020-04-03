import turtle
from tkinter import messagebox

win = turtle.Screen()
win.title("Strike")
win.setup(width=800,height=600)
win.bgcolor("green")
win.tracer(0)

#score
healthofgun2=turtle.Turtle()
healthofgun2.color("white")
healthofgun2.hideturtle()
healthofgun2.penup()
healthofgun2.goto(-350,0)
healthofgun2.write("Health of Player 2\n|||||",font=("Arial",24,"normal"))


healthofgun1=turtle.Turtle()
healthofgun1.color("white")
healthofgun1.hideturtle()
healthofgun1.penup()
healthofgun1.goto(20,0)
healthofgun1.write("Health of Player 1\n|||||",font=("Arial",24,"normal"))

#Gun1
Gun1 = turtle.Turtle()
Gun1.shape("square")
Gun1.color("white")
Gun1.penup()
Gun1.shapesize(stretch_wid=1,stretch_len=3)
Gun1.goto(100,-280)

#bullet1
Bullet1=turtle.Turtle()
Bullet1.shape("turtle")
Bullet1.color("white")
Bullet1.penup()
Bullet1.goto(100,-280)
Bullet1.y=0.9

#Gun2
Gun2=turtle.Turtle()
Gun2.shape("square")
Gun2.color("yellow")
Gun2.penup()
Gun2.shapesize(stretch_wid=1,stretch_len=3)
Gun2.goto(0,280)

#Bullet2
Bullet2=turtle.Turtle()
Bullet2.shape("turtle")
Bullet2.color("yellow")
Bullet2.penup()
Bullet2.goto(0,280)
Bullet2.y=1.1

#functions
def Gun1_move_left():
    x = Gun1.xcor()
    x -= 20
    Gun1.setx(x)

def Gun1_move_right():
    x = Gun1.xcor()
    x += 20
    Gun1.setx(x)

def Gun2_move_left():
    x = Gun2.xcor()
    x -= 40
    Gun2.setx(x)

def Gun2_move_right():
    x = Gun2.xcor()
    x += 40
    Gun2.setx(x)

#calling functions

win.listen()
win.onkeypress(Gun1_move_left,"a")
win.onkeypress(Gun1_move_right,"d")
win.onkeypress(Gun2_move_left,"Left")
win.onkeypress(Gun2_move_right,"Right")
health1=5
health2=5

while True:
    win.update()
    Bullet1.sety(Bullet1.ycor() + Bullet1.y)
    Bullet2.sety(Bullet2.ycor() - Bullet2.y)
    if Bullet1.ycor() >= 300:
        y = Gun1.ycor()
        x = Gun1.xcor()
        Bullet1.goto(x,y)

    if Bullet2.ycor() <= -300:
        y = Gun2.ycor()
        x = Gun2.xcor()
        Bullet2.goto(x,y)

    if Bullet1.ycor() >= 280 and (Bullet1.xcor() <= Gun2.xcor() + 33 and Bullet1.xcor() >= Gun2.xcor() - 33):
        health1-=1
        healthofgun2.clear()
        if health1 == 4:
            healthofgun2.write("Health of Player 2 \n||||",font=("Arial",24,"normal"))
        elif health1 == 3:
            healthofgun2.write("Health of Player 2 \n|||",font=("Arial",24,"normal"))
        elif health1== 2:
            healthofgun2.write("Health of Player 2 \n||",font=("Arial",24,"normal"))
        elif health1 == 1:
            healthofgun2.write("Health of Player 2 \n|",font=("Arial",24,"normal"))
        y = Gun1.ycor()
        x = Gun1.xcor()
        Bullet1.goto(x,y)

    if Bullet2.ycor() <= -280 and (Bullet2.xcor() <= Gun1.xcor() + 33 and Bullet2.xcor() >= Gun1.xcor() - 33):
        health2-=1
        healthofgun1.clear()
        if health2 == 4:
            healthofgun1.write("Health of Player 1\n||||",font=("Arial",24,"normal"))
        elif health2 == 3:
            healthofgun1.write("Health of Player 1\n|||",font=("Arial",24,"normal"))
        elif health2 == 2:
            healthofgun1.write("Health of Player 1\n||",font=("Arial",24,"normal"))
        elif health2 == 1:
            healthofgun1.write("Health of Player 1\n|",font=("Arial",24,"normal"))
        y = Gun2.ycor()
        x = Gun2.xcor()
        Bullet2.goto(x,y)
        
    if health1 == 0:
        messagebox.showinfo("Gameover","Target Demolished \nPlayer A wins")
        break
    
    if health2 == 0:
        messagebox.showinfo("Gameover","Target Demolished \nPlayer B wins")
        break
    
