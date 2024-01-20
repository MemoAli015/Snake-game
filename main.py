from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake game')
screen.tracer(0)

snakee = Snake()
food = Food()
scoreboard2 = ScoreBoard()


screen.listen()
screen.onkey(snakee.up,"Up")
screen.onkey(snakee.left, "Left")
screen.onkey(snakee.right, "Right")
screen.onkey(snakee.down, "Down")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snakee.move()
    if snakee.head.distance(food) < 15:
        scoreboard2.Clear_Screen()
        scoreboard2.IncraseScore()
        snakee.extend()
        food.refresh()
    if snakee.head.xcor() > 280 or snakee.head.xcor() < -280 or snakee.head.ycor() > 280 or snakee.head.ycor() < -280:
        game_is_on = False
        scoreboard2.game_over()

    for segment in snakee.segments:
        if segment == snakee.head:
            pass
        elif snakee.head.distance(segment) < 10:
            game_is_on = False
            scoreboard2.game_over()


screen.exitonclick()