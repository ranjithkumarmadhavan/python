import turtle
import time
from tkinter import messagebox
import winsound
import random

window = turtle.Screen()
window.setup(width=500, height= 600)
window.title("Ping pong")
window.bgcolor("red")
window.tracer(0)

player1 = window.textinput("Player 1","Enter player 1 name :")
player2 = window.textinput("Player 2","Enter player 2 name :")

def getReady():
    for i in reversed(range(3)):
        countDown = turtle.Turtle()
        countDown.hideturtle()
        countDown.color("white")
        countDown.write("Get Ready \n       {}".format(i+1),align="center",font=("Arial",20,"normal"))
        time.sleep(1)
        countDown.clear()

getReady()

# rectangle A
rectA = turtle.Turtle()
rectA.shape("square")
rectA.color("white")
rectA.speed(0)
rectA.penup()
rectA.shapesize(stretch_len=5,stretch_wid=1)
rectA.goto(0,280)

# rectangle B
rectB = turtle.Turtle()
rectB.shape("square")
rectB.color("white")
rectB.speed(0)
rectB.penup()
rectB.shapesize(stretch_len=5,stretch_wid=1)
rectB.goto(0, -280)

# ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.speed(0)
ball.penup()
ball.x = random.choice([-0.4,-0.3,-0.2,-0.1,0.1,0.2,0.3,0.4,0.5,0.6]) #0.4
ball.y = random.choice([-0.4,-0.5,-0.6,0.4,0.5,0.6]) 

# score board
score = turtle.Turtle()
score.hideturtle()
score.color("white")
score.speed(0)
score.penup()
score.goto(-250, -20)
player1Score = 0
player2Score = 0
score.write("Score board \n{} : {}\n{} : {}".format(player1,player1Score,player2,player2Score),align="left",font=("Arial",20,"normal"))

def moveRectALeft():
    x = rectA.xcor()
    x -= 50
    rectA.setx(x)

def moveRectARight():
    x = rectA.xcor()
    x += 50
    rectA.setx(x)

def moveRectBLeft():
    x = rectB.xcor()
    x -= 50
    rectB.setx(x)

def moveRectBRight():
    x = rectB.xcor()
    x += 50
    rectB.setx(x)

window.listen()
window.onkeypress(moveRectALeft,"a")
window.onkeypress(moveRectARight,"d")
window.onkeypress(moveRectBLeft,"Left")
window.onkeypress(moveRectBRight,"Right")

while True:
    window.update()

    ball.setx(ball.xcor() + ball.x)
    ball.sety(ball.ycor() + ball.y)

    if ball.xcor() >= 250:
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
        ball.x *= -1
    
    if ball.xcor() <= -250:
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
        ball.x *= -1

    if ball.ycor() >= 300:
        winsound.PlaySound("fade.wav",winsound.SND_ASYNC)
        ball.goto(0,0)
        ball.x = random.choice([-0.4,-0.3,-0.2,-0.1,0.1,0.2,0.3,0.4]) #0.4
        ball.y = random.choice([-0.4,-0.5,-0.6,0.4,0.5,0.6]) 
        player2Score += 1
        score.clear()
        score.write("Score board \n{} : {}\n{} : {}".format(player1,player1Score,player2,player2Score),align="left",font=("Arial",20,"normal"))

    if ball.ycor() <= -300:
        winsound.PlaySound("fade.wav",winsound.SND_ASYNC)
        ball.goto(0,0)
        ball.x = random.choice([-0.4,-0.3,-0.2,-0.1,0.1,0.2,0.3,0.4]) #0.4
        ball.y = random.choice([-0.4,-0.5,-0.6,0.4,0.5,0.6]) 
        score.clear()
        player1Score += 1
        score.write("Score board \n{} : {}\n{} : {}".format(player1,player1Score,player2,player2Score),align="left",font=("Arial",20,"normal"))

    if (ball.ycor() > 274 and ball.ycor() < 275) and (ball.xcor() < rectA.xcor() + 50 and ball.xcor() > rectA.xcor() - 50):
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
        ball.y *= -1

    if (ball.ycor() < -274 and ball.ycor() > -275) and (ball.xcor() < rectB.xcor() + 50 and ball.xcor() > rectB.xcor() - 50):
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
        ball.y *= -1

    if player1Score >= 5:
        winsound.PlaySound("applause.wav",winsound.SND_ASYNC)
        messagebox.showinfo("Game over","{} wins".format(player1))
        break

    if player2Score >= 5:
        winsound.PlaySound("applause.wav",winsound.SND_ASYNC)
        messagebox.showinfo("Game over","{} wins".format(player2))
        break