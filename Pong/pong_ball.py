from turtle import Turtle
import random

START_ANGLE = [45, 135, 225, 315]
game_on = True


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.speed("slowest")
        self.penup()
        self.setpos(0, 0)
        start = random.choice(START_ANGLE)
        self.setheading(start)

    def move(self, l_tab, r_tab):
        self.forward(20)
        if self.distance(r_tab) < 40:
            self.tab_angle()
        if self.distance(l_tab) < 40:
            self.tab_angle()
        if self.ycor() > 280 or self.ycor() < -280:
            self.wall_angle()

    def l_miss(self, point):
        if self.xcor() < -400:
            point()
            return True

    def r_miss(self, point):
        if self.xcor() > 400:
            point()
            return True

    def point(self):
        self.setpos(0, 0)
        start = random.choice(START_ANGLE)
        self.setheading(start)

    def wall_angle(self):
        before_hit = self.heading()
        if before_hit >= 0 and before_hit <= 90:
            after_hit = 270 + before_hit
        elif before_hit > 90 and before_hit <= 180:
            after_hit = 90 + before_hit
        elif before_hit > 180 and before_hit <= 270:
            after_hit = before_hit - 90
        elif before_hit > 270 and before_hit < 359:
            after_hit = before_hit - 270
        self.setheading(after_hit)

    def tab_angle(self):
        before_hit = self.heading()
        if before_hit >= 0 and before_hit <= 90:
            after_hit = 90 + before_hit
        elif before_hit > 90 and before_hit <= 180:
            after_hit = before_hit - 90
        elif before_hit > 180 and before_hit <= 270:
            after_hit = before_hit + 90
        elif before_hit > 270 and before_hit < 359:
            after_hit = before_hit - 90
        self.setheading(after_hit)
