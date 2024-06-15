# Importing requirments
from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time


# Creating and altering the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game Py")
screen.tracer(0)

# Adding objects into the game
snake = Snake()
food = Food()
score = Score()

# Creating game controls
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
# Launching the game
while game_on == True:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect colision with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.grow()
        score.score_update()
    # Detect collision with the wall
    if (
        snake.head.xcor() < -290
        or snake.head.xcor() > 290
        or snake.head.ycor() < -290
        or snake.head.ycor() > 290
    ):
        # game_on = False
        score.reset()
        snake.reset()
    # Looking for cannibalism
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            # game_on = False
            score.reset()
            snake.reset()


# Adding functionality to close the screen
screen.exitonclick()
