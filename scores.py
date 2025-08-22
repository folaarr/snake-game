from turtle import Turtle


class Scores(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("grey")
        self.up()
        self.sety(200)
        self.scores = 0
        self.refresh_scores()

    def refresh_scores(self):
        self.write(arg=f"Score: {self.scores}", align="center", font=("times new roman", 14, "normal"))

    def increase_score(self):
        self.scores += 1
        self.clear()
        self.refresh_scores()
