from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.ht()
        self.sety(265)
        self.score = 0


    def star_screen(self):
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, "center", ("Courier", 17, "normal"))

    def clear_screen(self):
        self.clear()
        self.score += 1
    
    def reset(self):
        self.clear()
        if self.score > self.high_score:
            self.score = str(self.score)
            with open("data.txt",mode="w") as file:
                self.high_score = file.write(self.score)
        self.score = 0
        self.star_screen()
        
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", False, "center", ("Courier", 17, "normal"))
