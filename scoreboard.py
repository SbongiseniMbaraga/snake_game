from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.goto(-10, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.get_num()}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.get_num():
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    @staticmethod
    def get_num():
        with open("data.txt") as data:
            number = data.read()
        return int(number)