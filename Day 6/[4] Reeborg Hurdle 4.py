#link: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

def turn_right():
    for i in range(3):
        turn_left()


def jump():
    turn_left()
    while wall_on_right():
        move()
    for i in range(2):
        turn_right()
        move()
    while wall_on_right() and not wall_in_front():
        move()
    if wall_in_front():
        turn_left()


while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()
