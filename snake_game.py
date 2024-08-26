from turtle import Screen
import time
from Snake import Play_snake, Complete_Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game!")

snake = Play_snake()

food = Food()
score = Scoreboard()


screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.left,"a")
screen.onkey(snake.right,"d")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.Move()
    score.star_screen()
    if Complete_Snake[0].distance(food) < 15:
        food.refresh_food()
        snake.extend()
        score.clear_screen()
    if Complete_Snake[0].xcor() > 285 or Complete_Snake[0].ycor() > 285 or Complete_Snake[0].ycor() < -285 or Complete_Snake[0].xcor() < -285:
        score.reset()
        snake.reset()
    for i in Complete_Snake[1:]:
        if Complete_Snake[0].distance(i) < 10:
            score.reset()
            snake.reset()


screen.exitonclick()