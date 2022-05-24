import turtle

# class Food():
class Food(turtle.Turtle):

    def __init__(self):
        super().__init__()
        #snake food
        # self.food = turtle.Turtle()
        self.speed(0)
        self.shape("square")
        self.color("red")
        self.penup()
        self.goto(0, 100)