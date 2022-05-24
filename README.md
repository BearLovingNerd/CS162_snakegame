# CS162_snakegame
A snake game that demonstrates class objects and importing files

A snake game using four imports

1) A snake file, containing a class object Snake. The snake handles keyboard inputs and extending itself
2) The food file, with class object Food. Grants points and lengthens the snake
3) The scoreboard, with class object ScoreBoard. Keeps track of the player's score and updates when you get food
4) and finall the main file, which compiles the other three files together to create a snake game.

Known bugs, the snake does not properly reset to full length after you game over. I kept incurring an IndexError in the snake's extend(): function, so I included an except/pass statement to ignore the bug
