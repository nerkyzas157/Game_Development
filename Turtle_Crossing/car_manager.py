from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
DEFAULT_CAR_HEADING = 180


class CarManager:
    def __init__(self):
        self.level = 1
        self.current_speed = STARTING_MOVE_DISTANCE
        self.new_speed = MOVE_INCREMENT * self.level
        self.cars = []
        self.create_car()

    def create_car(self):
        car = Turtle()
        car.setheading(DEFAULT_CAR_HEADING)
        car.penup()
        car.shape("square")
        car.shapesize(stretch_len=2.5, stretch_wid=1)
        rand_color = random.choice(COLORS)
        y_coordinate = random.randrange(-260, 260, 20)
        car.setpos(320, y_coordinate)
        car.color(rand_color)
        self.cars.append(car)

    def move(self):
        for i in range(len(self.cars) - 1):
            self.cars[i].forward(self.current_speed)

    def new_level(self):
        self.current_speed += self.new_speed
        self.level += 1
