import time
from turtle import Screen

from scoreboard import Scoreboard
from snake import Snake
from food import Food

#screen object
screen = Screen()

#setting up screen
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My Snake Game")

#objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()


#setting arrow keys
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

#setting wasd keys
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True
while game_is_on:
    #for smooth transition
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision of food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with tail
                    #python slicing
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()