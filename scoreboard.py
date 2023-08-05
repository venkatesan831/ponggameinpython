from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.update()

    def update(self):
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("courier", 80, "normal"))
        self.hideturtle()
        self.goto(100,200)
        self.write(self.r_score, align="center", font=("courier", 80, "normal"))

    def increase_lscore(self):
        self.l_score += 1
        self.clear()
        self.update()

    def increase_rscore(self):
        self.r_score += 1
        self.clear()
        self.update()