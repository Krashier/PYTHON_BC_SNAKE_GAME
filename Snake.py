from turtle import Turtle
Complete_Snake = []
position = [(0,0),(-20,0),(-40,0)]

class Play_snake:
    def __init__(self):
        self.Snake()

    def Snake(self):
        for i in position:
            self.add_segment(i)

    def add_segment(self,position):
        global Complete_Snake
        size_snake = Turtle("square")
        size_snake.color("white")
        size_snake.penup()
        size_snake.setpos(position)
        Complete_Snake.append(size_snake)
        
    def extend(self):
        self.add_segment(Complete_Snake[-1].position())

    def Move(self):
        for i in range(len(Complete_Snake)-1,0,-1):
            x_cord = Complete_Snake[i-1].xcor()
            y_cord = Complete_Snake[i-1].ycor()
            Complete_Snake[i].goto(x_cord,y_cord)
        Complete_Snake[0].forward(20)

    def up(self):
        if Complete_Snake[0].heading() != 270:
            Complete_Snake[0].setheading(90)
    def down(self):
        if Complete_Snake[0].heading() != 90:
            Complete_Snake[0].setheading(270)
    def left(self):
        if Complete_Snake[0].heading() != 0:
            Complete_Snake[0].setheading(180)
    def right(self):
        if Complete_Snake[0].heading() != 180:
            Complete_Snake[0].setheading(0)

    def reset(self):
        for i in Complete_Snake:
            i.goto(1000,1000)
        Complete_Snake.clear()
        self.Snake()