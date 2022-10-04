import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkeypress(player.go_up, 'Up')


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    
    if player.is_at_finish_line():
        car_manager.level_up()
        scoreboard.update_score()
        player.go_to_start()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()