import time
import pygame
from turtle import Screen,Turtle

from scoreboard import Scoreboard
from snake import Snake
from food import Food

pygame.mixer.init()
eat_sound = pygame.mixer.Sound("eat.wav")
collision_sound = pygame.mixer.Sound("collision.wav")

#screen object
screen = Screen()

#setting up screen
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My Snake Game")

border = Turtle()
border.penup()
border.goto(-290, -290)
border.pendown()
border.goto(290, -290)
border.goto(290, 290)
border.goto(-290, 290)
border.goto(-290, -290)
border.hideturtle()

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
game_speed = 0.1
while game_is_on:
    #for smooth transition
    screen.update()
    time.sleep(game_speed)
    snake.move()

    # Detect collision of food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        game_speed *= 0.95
        eat_sound.play()


    #Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        collision_sound.play()
        scoreboard.reset_score()
        snake.reset()
        game_speed = 0.1


    #Detect collision with tail
                    #python slicing
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            collision_sound.play()
            scoreboard.reset_score()
            snake.reset()
            game_speed = 0.1


screen.exitonclick()