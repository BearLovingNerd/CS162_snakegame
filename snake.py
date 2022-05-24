import turtle

POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        # snake head
        # # self.head = turtle.Turtle()
        # self.head.speed(0)
        # self.head.shape("square")
        # self.head.color("black")
        # self.head.penup
        # self.head.goto(0, 0)
        # self.head.direction = "stop"
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # Create the body
    def create_snake(self):
        for position in POSITION:
            self.add_segment(position)

    # add a new segment
    def add_segment(self, position):
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("black")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        try:
            self.add_segment(self.segments[-1].position())
        except IndexError:
            pass

    # Functions
    def go_up(self):
        # if self.head.direction != "down":
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def go_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def go_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def go_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move(self):
        # move the segments in reverse order
        for index in range(len(self.segments) - 1, 0, -1):
            x = self.segments[index - 1].xcor()
            y = self.segments[index - 1].ycor()
            self.segments[index].goto(x, y)
        self.head.forward(20)
