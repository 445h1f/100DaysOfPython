from turtle import Turtle, Screen

STARTING_X_POSITION = [20, 0, -20] # default x coordinates for first 3 segments of snake
MOVE_DISTANCE = 20 # pixels to be moved
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self, color):
        self.segments = [] # list to store all snake segments (as turtle object)
        self.color = color
        self.create_snake()
        self.head = self.segments[0] # assigning head to first segment

    def create_snake(self):
        """Creating first 3 snake segments."""
        for i in range(3):
            self.add_segment((STARTING_X_POSITION[i], 0))

    def add_segment(self, position):
        """Adding Snake Segment!"""
        segment = Turtle(shape='square')
        segment.penup()
        segment.color(self.color)
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        """Extending snake by adding snake segment after the last snake segment."""
        tail_position = self.segments[-1].position() # getting last segment position
        self.add_segment(tail_position) # adding new segment at the last

    def move(self):
        f"""Moving every segments {MOVE_DISTANCE} forward!"""
        segments = self.segments # getting all segments
        for seg_num in range(len(segments)-1, 0, -1):
            new_position = segments[seg_num-1].position()
            segments[seg_num].goto(new_position)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Turning snake UP if it is not moving DOWN."""
        if self.head.heading() != DOWN: #when down dont go up
            self.head.setheading(UP)

    def down(self):
        """Turning snake DOWN if it is not moving UP."""
        if self.head.heading() != UP: #when up dont go down
            self.head.setheading(DOWN)

    def right(self):
        """Turning snake RIGHT if it is not moving LEFT."""
        if self.head.heading() != LEFT: #when left dont go right
            self.head.setheading(RIGHT)

    def left(self):
        """Turning snake LEFT if it is not moving RIGHT."""
        if self.head.heading() != RIGHT: #when right dont go left
            self.head.setheading(LEFT)