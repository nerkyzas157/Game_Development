from turtle import Screen
from tabs import Left_Tab, Right_Tab, Middle_Line
from score import Score
from pong_ball import Ball
import time

# Creating and altering the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Adding objects into the game
middle = Middle_Line()
score = Score()
ltab = Left_Tab()
rtab = Right_Tab()
ball = Ball()

# Creating game controls
screen.listen()
screen.onkey(ltab.up, "w")
screen.onkey(ltab.down, "s")
screen.onkey(rtab.up, "Up")
screen.onkey(rtab.down, "Down")

game_on = True
middle.job()
# Launching the game
while game_on == True:
    screen.update()
    time.sleep(0.07)
    ball.move(ltab, rtab)
    if ball.l_miss(score.r_score_update) == True:
        ball.point()
    if ball.r_miss(score.l_score_update) == True:
        ball.point()
    if score.game_over() == True:
        game_on = False


screen.exitonclick()
