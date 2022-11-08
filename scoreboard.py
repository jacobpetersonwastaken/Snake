from turtle import Turtle, onscreenclick

class Scoreboard(Turtle):
    def __init__(self, SCREEN_HEIGHT):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x=0, y=(SCREEN_HEIGHT / 2) - 30)
        self.update_scoreboard()

    def update_scoreboard(self):
        with open('data.csv', 'r')as f:
            hs = f.read()
        if hs == '':
            hs = 0

        self.write(f"Score: {self.score} | Highscore: {hs}", align="center", font=("Arial", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.color("red")
        self.penup()
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=("Arial", 50, "normal"))


        with open('data.csv', 'w')as f:
            f.write(str(self.score))


