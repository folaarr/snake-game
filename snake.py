from turtle import Turtle

STARTING_POSITIONS = [(-40, 0), (-20, 0), (0, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.up()
            new_segment.goto(position)
            self.segments.append(new_segment)
        self.head = self.segments[-1]

    def move(self):
        for segment in self.segments[0:len(self.segments) - 1]:
            segment.goto(self.segments[self.segments.index(segment) + 1].position())
        if self.head.xcor() > 240:
            self.head.setx(-240)
        elif self.head.xcor() < -240:
            self.head.setx(240)
        elif self.head.ycor() > 220:
            self.head.sety(-220)
        elif self.head.ycor() < -220:
            self.head.sety(220)
        else:
            self.head.fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.seth(90)

    def left(self):
        if self.head.heading() != 0:
            self.head.seth(180)

    def down(self):
        if self.head.heading() != 90:
            self.head.seth(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.seth(0)

    def grow(self):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.up()
        new_segment.goto(self.segments[-1].position())
        new_segment.seth(self.segments[-1].heading())
        self.segments.append(new_segment)
        self.head = new_segment
