import time
from snake import Snake
from food import Food
from scoreboard import Score
from turtle import Screen, Turtle
from themes import THEMES

screen = Screen()
HEIGHT = 600
WIDTH = 600
# sets screen size to 600x600
screen.setup(height=HEIGHT, width=WIDTH)

# asks user to choose difficulty level
difficulty = int(screen.numinput(title=f'Difficulty', prompt='1: Easy\n2: Medium\n3: Hard', default=3, minval=1, maxval=3))


# sets sreen refresh time according to difficulty level
# more difficulty less time
if difficulty == 1:
    SLEEPTIME = 0.3
elif difficulty == 2:
    SLEEPTIME = 0.2
else:
    SLEEPTIME = 0.1

# theme part
# asking user for choosing the theme
themes_str = ''
themes_title_list = []
n = 1
for t in THEMES:
    themes_str += f'{n}: {t}\n'
    themes_title_list.append(t)
    n += 1

theme = int(screen.numinput(title='Choose Theme: ', prompt=themes_str, minval=1, maxval=len(themes_title_list), default=1))

# getting theme data of chosen them
theme = THEMES[themes_title_list[theme-1]]

background_color = theme['background']
snake_color = theme['snake']
food_color = theme['food']
text_color = theme['text']


screen.bgcolor(background_color) # sets bg color
screen.title('My Snake Game') # sets title of window
screen.tracer(0)


# starts listening to key strokes
screen.listen()


# game objects
snake = Snake(snake_color)
food = Food(food_color)
scoreboard = Score(text_color)
screen.update()

# key press events
screen.onkey(snake.up, 'Up') # move up
screen.onkey(snake.down, 'Down') # move down
screen.onkey(snake.left, 'Left') # move left
screen.onkey(snake.right, 'Right') # move right
screen.onkey(scoreboard.pause_resume, 'space') # pause/resume

# starting the game

game_is_on = True
# running the game until it is on
while game_is_on:
    # updating the screen on every iteration
    screen.update()

    # if game is not paused continuing the game stuffs
    if not scoreboard.game_pause:
        # setting sleeptime for next screen refresh defined in diffculty level
        time.sleep(SLEEPTIME)

        # starts snake moving
        snake.move()

        # detecting collison with food
        if snake.head.distance(food) < 15:
            snake.extend() # adding another square to increase snake size
            food.refresh() # randomly placing food in screen
            scoreboard.increase_score() # adding 1 to the score

        # detecting collision with walls
        if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
            game_is_on = False # becuase snake hits the wall
            scoreboard.game_over() # game over display on screen

        # detecting collision with any segment
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False # game over because snake collided with his own body/square blocks.
                scoreboard.game_over()
    else:
        # if game is pause, checking every second for resume
        time.sleep(1)


# exits screen on click
screen.exitonclick()