from turtle import Turtle
from typing import List, Tuple

COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_FORWARD = 20


class Snake(Turtle):
    body: List[Turtle]
    speed: float

    def __init__(self) -> None:
        super().__init__()
        self.body = []
        self.speed = 0.5
        self.create_body()

    def create_body(self) -> None:
        for position in COORDINATES:
            self.add_segment(position)

    def add_segment(self, position: Tuple[int]) -> None:
        new_body = Turtle("square")
        new_body.color("white")
        new_body.pu()
        new_body.goto(position)
        self.body.append(new_body)

    def extend(self) -> None:
        self.add_segment(self.body[-1].position())
        self.speed *= 0.9

    def move(self) -> None:
        for i in range(len(self.body) - 1, 0, -1):
            new_x = self.body[i - 1].xcor()
            new_y = self.body[i - 1].ycor()
            self.body[i].goto(new_x, new_y)
        self.body[0].forward(MOVE_FORWARD)

    def up(self) -> None:
        current_heading = self.body[0].heading()
        if current_heading == 0 or current_heading == 180:
            self.body[0].setheading(90)

    def left(self) -> None:
        current_heading = self.body[0].heading()
        if current_heading == 90 or current_heading == 270:
            self.body[0].setheading(180)

    def down(self) -> None:
        current_heading = self.body[0].heading()
        if current_heading == 0 or current_heading == 180:
            self.body[0].setheading(270)

    def right(self) -> None:
        current_heading = self.body[0].heading()
        if current_heading == 90 or current_heading == 270:
            self.body[0].setheading(0)

    def reset_snake(self) -> None:
        for body in self.body:
            body.goto(1000,1000)
        self.body.clear()
        self.create_body()
