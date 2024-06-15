from turtle import Turtle

UP = 90
DOWN = 270
MOVE_DISTANCE = 40


class Tab(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.setheading(UP)

    def up(self):
        self.setheading(UP)
        self.forward(MOVE_DISTANCE)

    def down(self):
        self.setheading(DOWN)
        self.forward(MOVE_DISTANCE)

    def r_up(self):
        self.setheading(UP)
        self.forward(MOVE_DISTANCE)

    def r_down(self):
        self.setheading(DOWN)
        self.forward(MOVE_DISTANCE)


class Middle_Line(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor("white")

    def job(self):
        self.teleport(0, 400)
        self.setheading(270)
        for i in range(20):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)


class Left_Tab(Tab):
    def __init__(self):
        super().__init__()
        self.setpos(-380, -50)


class Right_Tab(Tab):
    def __init__(self):
        super().__init__()
        self.setpos(370, 50)
