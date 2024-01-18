import time
from turtle import Turtle, Screen
from scoreboard import Score
from food import Food
from snake import Snake

if __name__ == '__main__':

    # build the screen
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My snake game")
    screen.tracer(0)

    # create the snake, food and score
    snake = Snake()
    food = Food()
    score = Score()

    # listen for key presses
    screen.onkey(key="Up", fun=snake.up)
    screen.onkey(key="Down", fun=snake.down)
    screen.onkey(key="Left", fun=snake.left)
    screen.onkey(key="Right", fun=snake.right)

    # Score board
    score_val = 0
    score.score_write(score_val)

    # game loop
    game_is_on = True
    while game_is_on:
        snake.snake_move()
        screen.update()
        time.sleep(0.15)
        screen.listen()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            score_val += 1
            score.score_write(score_val)
            # snake.extend()

        # Detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            game_is_on = False
            score.game_over()

        # Detect collision with tail
        for segment in snake.segments:
            if segment == snake.head:
                pass
            elif snake.head.distance(segment) < 10:
                game_is_on = False
                score.game_over()

    screen.exitonclick()
