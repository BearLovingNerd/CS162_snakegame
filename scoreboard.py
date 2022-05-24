import turtle
import random

class ScoreBoard:
    def __init__(self):
        self.score = 0
        self.high_score = 0

        self.sc = turtle.Turtle()
        self.sc.speed(0)
        self.sc.shape("square")
        self.sc.color("black")
        self.sc.penup()
        self.sc.hideturtle()
        self.sc.goto(0, 260)
        self.sc.write("score: 0  High score: 0", align="center", font=("ds-digital", 24, "normal"))

    def draw_score(self):
        self.sc.clear()
        self.sc = turtle.Turtle()
        self.sc.speed(0)
        self.sc.shape("square")
        self.sc.color("black")
        self.sc.penup()
        self.sc.hideturtle()
        self.sc.goto(0, 260)
        self.sc.write("score: 0  High score: 0", align="center", font=("ds-digital", 24, "normal"))

    def update_score(self):
        self.sc.clear()
        self.sc = turtle.Turtle()
        self.sc.speed(0)
        self.sc.shape("square")
        self.sc.color("black")
        self.sc.penup()
        self.sc.hideturtle()
        self.sc.goto(0, 260)
        self.sc.write("Score: {}  High score: {}".format(self.score, self.high_score), align="center", font=("ds-digital", 24, "normal"))