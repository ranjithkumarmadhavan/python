import turtle
from tkinter import messagebox

win = turtle.Screen()
win.title("Strike")
win.setup(width=800,height=600)
win.bgcolor("green")
win.tracer(0)

#score
healthoftarget=turtle.Turtle()
healthoftarget.color("white")
healthoftarget.hideturtle()
healthoftarget.penup()
healthoftarget.goto(-350,0)
healthoftarget.write("Health \n|||||",font=("Arial",24,"normal"))

#Gun
Gun = turtle.Turtle()
Gun.shape("square")
Gun.color("white")
Gun.penup()
Gun.shapesize(stretch_wid=2,stretch_len=2)
Gun.goto(100,-280)

#bullet
Bullet=turtle.Turtle()
Bullet.shape("turtle")
Bullet.color("white")
Bullet.penup()
Bullet.goto(100,-280)
Bullet.y=1.9

#Target
target=turtle.Turtle()
target.shape("square")
target.color("yellow")
target.penup()
target.shapesize(stretch_wid=1,stretch_len=3)
target.goto(0,280)

#functions
def bullet_move_left():
    x = Gun.xcor()
    x -= 20
    Gun.setx(x)

def bullet_move_right():
    x = Gun.xcor()
    x += 20
    Gun.setx(x)

def target_move_left():
    x = target.xcor()
    x -= 40
    target.setx(x)

def target_move_right():
    x = target.xcor()
    x += 40
    target.setx(x)

#calling functions

win.listen()
win.onkeypress(bullet_move_left,"a")
win.onkeypress(bullet_move_right,"d")
win.onkeypress(target_move_left,"Left")
win.onkeypress(target_move_right,"Right")
health=5

while True:
    win.update()
    Bullet.sety(Bullet.ycor() + Bullet.y)
    if Bullet.ycor() >= 300:
        y = Gun.ycor()
        x = Gun.xcor()
        Bullet.goto(x,y)

    if Bullet.ycor() >= 280 and (Bullet.xcor() <= target.xcor() + 33 and Bullet.xcor() >= target.xcor() - 33):
        health-=1
        healthoftarget.clear()
        if health == 4:
            healthoftarget.write("Health \n||||",font=("Arial",24,"normal"))
        elif health == 3:
            healthoftarget.write("Health \n|||",font=("Arial",24,"normal"))
        elif health == 2:
            healthoftarget.write("Health \n||",font=("Arial",24,"normal"))
        elif health == 1:
            healthoftarget.write("Health \n|",font=("Arial",24,"normal"))
        y = Gun.ycor()
        x = Gun.xcor()
        Bullet.goto(x,y)
        
    if health == 0:
        messagebox.showinfo("Gameover","Target Demolished")
        break
    
