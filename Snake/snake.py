from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        lenght = 3
        seg_count = 0
        for i in range(lenght):
            segment = Turtle()
            segment.penup()
            segment.shape("square")
            segment.color("white")
            if len(self.snake_body) >= 1:
                seg_count += 1
                segment.setpos(0 - (20 * seg_count), 0)
                self.snake_body.append(segment)
            else:
                segment.setpos(0, 0)
                self.snake_body.append(segment)

    def reset(self):
        for i in self.snake_body:
            i.hideturtle()
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
        self.head.goto(0, 0)

    def move(self):
        for i in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[i - 1].xcor()
            new_y = self.snake_body[i - 1].ycor()
            self.snake_body[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def grow(self):
        segment = Turtle()
        segment.penup()
        segment.shape("square")
        segment.color("white")
        segment.setpos(self.snake_body[-1].xcor(), self.snake_body[-1].ycor())
        self.snake_body.append(segment)
