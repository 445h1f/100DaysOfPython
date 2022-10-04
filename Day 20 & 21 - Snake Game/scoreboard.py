from turtle import Turtle
import time

ALIGNMENT = 'center'
FONT = ('Fira Code', 18, 'bold')


class Score(Turtle):
    """Score Management"""
    def __init__(self, color):
        super().__init__()
        self.score = 0 # setting score to 0 at the start
        self.highest = self.get_highscore()
        self.penup()
        self.hideturtle() # hiding the turtle on screen
        self.color(color) # setting score text color as per theme
        self.update() # updating the screen
        self.game_pause = False
        self.game_on = True

    def get_highscore(self):
        """Getting the highest score!"""
        with open('highscore.txt') as r:
            highscore = r.read()
            return int(highscore)

    def update_highscore(self):
        """Updating high score!"""
        with open('highscore.txt', 'w+') as w:
            w.write(str(self.highest))

    def update(self):
        # sending turtle to top middle where it'll display score
        self.goto(0, 270)
        self.clear()
        if self.score > self.highest:
            self.highest = self.score
            self.update_highscore()
        self.write(f'Score: {self.score} | Highest: {self.highest}', align=ALIGNMENT, font=FONT)


    def increase_score(self):
        """Increases score by 1"""
        self.score += 1
        self.update()


    def game_over(self):
        """Writing Game Over at the center."""
        self.update()
        self.goto(0, 0) #center coordinates
        self.write('GAME OVER!', align=ALIGNMENT, font=FONT)
        self.game_on = False

    def pause_resume(self):
        """Pausing/Resuming game."""
        if not self.game_on:
            return
        self.update()
        self.goto(0, 0)
        if not self.game_pause: # pausing if game is not pause
            self.write('PAUSE!', align=ALIGNMENT, font=FONT)
            self.game_pause = True
        else:
            self.write('RESUMED!', align=ALIGNMENT, font=FONT) # resuming if game is paused
            time.sleep(0.5) # resuming after 0.5 seconds so that user can be ready
            self.update()
            self.game_pause = False


