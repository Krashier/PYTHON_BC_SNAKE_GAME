from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh_food()

    def refresh_food(self):
        x_rand_cord = random.randint(-280,280)
        y_rand_cord = random.randint(-280,280)
        self.goto(x_rand_cord,y_rand_cord)
        