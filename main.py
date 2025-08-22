from turtle import Screen, done
from snake import Snake
from time import sleep
from food import Food
from scores import Scores

interface = Screen()
interface.title("Snake Game By Folajimi.")
interface.setup(width=480, height=440)
interface.bgcolor("black")
interface.tracer(0)

snake = Snake()

food = Food()

scores = Scores()

interface.listen()
interface.onkey(fun=snake.up, key="Up")
interface.onkey(fun=snake.left, key="Left")
interface.onkey(fun=snake.down, key="Down")
interface.onkey(fun=snake.right, key="Right")

game_on = True

while game_on:
    snake.move()
    sleep(0.25)
    interface.update()

    # Detect collision with food.
    if snake.head.distance(food) < 18:
        snake_print = []
        for segment in snake.segments:
            segment_position = segment.position()
            snake_print.append(segment_position)
        food.reset_food()
        while food.position() in snake_print:
            food.reset_food()
        scores.increase_score()
        snake.grow()

done()
