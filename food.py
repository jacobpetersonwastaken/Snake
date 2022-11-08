from turtle import Turtle
from random import randint



class Food(Turtle):
    def __init__(self,SCREEN_HEIGHT, SCREEN_WIDTH):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.refresh(SCREEN_HEIGHT, SCREEN_WIDTH)

    def refresh(self, SCREEN_HEIGHT, SCREEN_WIDTH):
        x = (SCREEN_WIDTH / 2) -20
        negative_x = x * -1
        y = (SCREEN_HEIGHT / 2) -20
        negative_y = y * -1
        self.goto(x=randint(negative_x, x), y=randint(negative_y,y))
