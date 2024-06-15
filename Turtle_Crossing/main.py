import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, "Up")


game_is_on = True
car_loop = 0
while game_is_on:
    x = player.ycor
    time.sleep(0.1)
    screen.update()
    if car_loop % 3 == 0:
        car_manager.create_car()
    car_manager.move()
    car_loop += 1
    if player.finish() == True:
        scoreboard.level_up()
        car_manager.new_level()
    if player.crash(car_manager.cars) == True:
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()
