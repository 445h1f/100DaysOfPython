#link: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json

def turn_right():
    for i in range(3):
        turn_left()


def jump():
    turn_left()
    move()
    for i in range(2):
        turn_right()
        move()
    turn_left()


while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()
