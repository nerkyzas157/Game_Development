from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
DEFAULT_HEADING = 90


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.setheading(DEFAULT_HEADING)
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.setpos(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def finish(self):
        if self.ycor() == FINISH_LINE_Y:
            self.setpos(STARTING_POSITION)
            return True

    def crash(self, cars):
        for i in cars:
            for l in range(int(i.ycor()) - 10, int(i.ycor()) + 11):
                if self.ycor() == l:
                    if self.distance(i) < 25:
                        return True
