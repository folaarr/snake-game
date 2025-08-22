from turtle import Turtle
from random import randrange


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.63, stretch_len=0.63)
        self.color("MediumSlateBlue")
        self.up()
        while self.xcor() in [-40, -20, 0] and self.ycor() == 0:
            self.reset_food()

    def reset_food(self):
        self.goto(randrange(-160, 180, 20), randrange(-160, 180, 20))
