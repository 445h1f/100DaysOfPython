from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-290, 260)
        self.level = 0
        self.update_score()

    def update_score(self):
        self.level += 1
        self.clear()
        self.write(f'Level: {self.level}', align='left', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER!', align='center', font=FONT)
