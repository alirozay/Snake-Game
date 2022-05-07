from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


is_game_on = True
timer = 0.5
screen = Screen()
screen.tracer(0)
simon_the_snake = Snake()
food = Food()
score = ScoreBoard()

screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.listen()
screen.onkeypress(fun=simon_the_snake.up, key="Up")
screen.onkeypress(fun=simon_the_snake.left, key="Left")
screen.onkeypress(fun=simon_the_snake.down, key="Down")
screen.onkeypress(fun=simon_the_snake.right, key="Right")

while is_game_on:
    screen.update()
    time.sleep(simon_the_snake.speed)
    simon_the_snake.move()
    if simon_the_snake.body[0].distance(food) < 15:
        food.refresh()
        simon_the_snake.extend()
        score.update()
    if simon_the_snake.body[0].xcor() > 280 or \
            simon_the_snake.body[0].xcor() < -280 or \
            simon_the_snake.body[0].ycor() > 280 or \
            simon_the_snake.body[0].ycor() < -280:
        score.game_over()
        is_game_on = False

    for body in simon_the_snake.body[1:]:
        if simon_the_snake.body[0].distance(body) < 15:
            score.game_over()
            is_game_on = False


screen.exitonclick()
