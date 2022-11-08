from turtle import Turtle, Screen


class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("red")
        self.penup()
        self.write(f"Game Over", align="center", font=("Arial", 50, "normal"))
        self.color("white")

        self.penup()
        self.goto(x=0, y=-100)
        self.write(f"Play again?", align="center", font=("Arial", 20, "normal"))
        self.boxes()

    def boxes(self):
        play_box_x = -100
        play_box_y = -100
        for i in range(2):
            self.showturtle()
            self.shape("circle")
            self.color("white")
            self.penup()
            self.goto(x=play_box_x, y=play_box_y)
            play_box_x += 200
