import turtle
from turtle import colormode, Screen, onscreenclick

from random import randrange
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

FOOD_DISTANCE = 20
alive = True
colormode(255)
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("snake boiz")
scoreboard = Scoreboard(SCREEN_HEIGHT)
food = Food(SCREEN_HEIGHT, SCREEN_WIDTH)
tim = Snake()


game_is_on = True
screen.listen()
screen.tracer(0)
screen.onkeypress(key='Up', fun=tim.up)
screen.onkeypress(key='Down', fun=tim.down)
screen.onkeypress(key='Left', fun=tim.left)
screen.onkeypress(key='Right', fun=tim.right)


while game_is_on:
    screen.update()
    time.sleep(.1)
    tim.move()

    if tim.head.distance(food) < FOOD_DISTANCE:
        food.refresh(SCREEN_HEIGHT, SCREEN_WIDTH)
        tim.extend()
        scoreboard.increase_score()
    if tim.head.xcor() > (SCREEN_WIDTH / 2) or tim.head.xcor() < (SCREEN_WIDTH / 2) * -1 or tim.head.ycor() > (SCREEN_HEIGHT / 2) or tim.head.ycor() < (SCREEN_HEIGHT / 2) * -1:
        scoreboard.game_over()
        game_is_on = False

    for i in tim.snake_list[1:]:
        if tim.head.distance(i) < 10:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()
