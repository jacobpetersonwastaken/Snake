from turtle import Turtle, colormode
from random import randrange

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]
        self.multiplier = 1

    def create_snake(self):
        for i in STARTING_POSITION:
            self.add_segment(i)

    def rand_color(self):
        r = randrange(256)
        g = randrange(256)
        b = randrange(256)
        return r, g, b

    def add_segment(self, i):
        snake = Turtle(shape="square")
        snake.penup()
        snake.color(self.rand_color())
        snake.goto(i)
        self.snake_list.append(snake)

    def extend(self):
        for i in range(self.multiplier):
            self.add_segment(self.snake_list[-1].position())
        self.multiplier += 0

    def move(self):
        for i in range(len(self.snake_list) - 1, 0, -1):
            new_x = self.snake_list[i - 1].xcor()
            new_y = self.snake_list[i - 1].ycor()
            self.snake_list[i].goto(new_x, new_y)
        self.snake_list[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.snake_list[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.snake_list[0].setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.snake_list[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.snake_list[0].setheading(RIGHT)


