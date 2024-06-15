import turtle
import random

screen = turtle.Screen()
screen.setup(width=700, height=500)
start = True
speed = [0, 5, 10, 15, 20, 25, 30]

red = turtle.Turtle()
red.color("red")
red.shape("turtle")

yellow = turtle.Turtle()
yellow.color("yellow")
yellow.shape("turtle")

green = turtle.Turtle()
green.color("green")
green.shape("turtle")

blue = turtle.Turtle()
blue.color("blue")
blue.shape("turtle")

black = turtle.Turtle()
black.color("black")
black.shape("turtle")


def set_start():
    finish_line()
    red.penup()
    red.teleport(-375, 200)
    yellow.penup()
    yellow.teleport(-375, 100)
    green.penup()
    green.teleport(-375, 0)
    blue.penup()
    blue.teleport(-375, -100)
    black.penup()
    black.teleport(-375, -200)


def finish_line():
    line = turtle.Turtle()
    line.hideturtle()
    line.teleport(300, 400)
    line.setheading(270)
    line.forward(800)


def finish():
    global start
    global winner
    if red.xcor() >= 290:
        start = False
        winner = "red"
    elif yellow.xcor() >= 290:
        start = False
        winner = "yellow"
    elif green.xcor() >= 290:
        start = False
        winner = "green"
    elif blue.xcor() >= 290:
        start = False
        winner = "blue"
    elif black.xcor() >= 290:
        start = False
        winner = "black"


def race():
    global bet
    bet = screen.textinput(
        title="Betting time", prompt="Place your bet: (red/yellow/green/blue/black)"
    ).lower()
    set_start()
    while start == True:
        red_speed = random.choice(speed)
        red.forward(red_speed)
        yellow_speed = random.choice(speed)
        yellow.forward(yellow_speed)
        green_speed = random.choice(speed)
        green.forward(green_speed)
        blue_speed = random.choice(speed)
        blue.forward(blue_speed)
        black_speed = random.choice(speed)
        black.forward(black_speed)
        finish()
    if bet == winner:
        print("\n\nYour bet won!")
    else:
        print(f"\n\nYour bet lost. The winner was {winner}.")


race()
screen.exitonclick()
