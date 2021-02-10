from turtle import Screen
from food import Food
import time
from snake import Snake

#screen size color
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

#objects
snake = Snake()
snake.create_snake()
snake.new_position()
food = Food()

#im looking for input
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

#moves the snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    #Detect the collision with food
    if snake.head.distance(food) < 15:
        food.refresh()

screen.exitonclick()