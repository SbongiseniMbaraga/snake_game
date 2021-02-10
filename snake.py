from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.turtle_objects = []
        self.create_snake()
        self.head = self.turtle_objects[0]

    def create_snake(self):
        for turtle_index in range(0, 3):
            new_turtle = Turtle()
            new_turtle.shape("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.resizemode("user")
            new_turtle.shapesize(1, 1)
            new_turtle.position()
            self.turtle_objects.append(new_turtle)

    def new_position(self):
        count = 0
        y_position = 0
        x_position = 0

        for item in self.turtle_objects:
            count += 1
            item.position()
            if count > 1:
                x_position += -20
                item.setpos(y=y_position, x=x_position)

    def move_snake(self):
        for t_num in range(len(self.turtle_objects) - 1, 0, -1):
            new_x = self.turtle_objects[t_num - 1].xcor()
            new_y = self.turtle_objects[t_num - 1].ycor()
            self.turtle_objects[t_num].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
