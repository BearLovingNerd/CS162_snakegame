# outside imports
import time
import random
import turtle
# in file imports
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# Create objects
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

#screen init
wn = turtle.Screen()
wn.title("Snakey Game")
wn.bgcolor('yellow')
wn.setup(width=600, height=600)
wn.tracer(0)

#keyboard bindings
wn.listen()
wn.onkeypress(snake.go_up, "w")
wn.onkeypress(snake.go_down, "s")
wn.onkeypress(snake.go_left, "a")
wn.onkeypress(snake.go_right, "d")

#reset delay
delay = 0.1

#main loop
while True:
    wn.update()
    time.sleep(delay)
    snake.move()

    #check collision with border
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        time.sleep(1)
        snake.head.goto(0, 0)

        #hide the segment of body
        for segment in snake.segments:
            segment.goto(1000, 1000) #off screen
        #clear the segments
        snake.segments.clear()

        #reset score
        scoreboard.draw_score()

        #reset delay
        delay = 0.1

        scoreboard.update_score()


    # check collision with food
    if snake.head.distance(food) < 10:
        # move the food to a random place
        x = random.randint(-14, 14)*20
        y = random.randint(-14, 14)*20
        food.goto(x, y)

        snake.extend()

        # increase speed
        delay -= 0.001

        # increase the score
        scoreboard.score += 10

        if scoreboard.score > scoreboard.high_score:
            scoreboard.high_score = scoreboard.score
        scoreboard.update_score()

    # check collision with body
    for segment in snake.segments:

        # If the segment is the head
        if segment == snake.head:
            pass
        # If segment is less than 20 within the head
        elif snake.head.distance(segment) < 10:
        # if segment.distance(snake.head) < 20:
            time.sleep(1)
            snake.head.goto(0, 0)
    
            # #hide segments
            for segment in snake.segments:
                segment.goto(1000, 1000) #off screen
            snake.segments.clear()
            scoreboard.score = 0
            delay = 0.1

            # update score
            scoreboard.update_score()
wn.mainloop()