from turtle import Turtle

class ScoreBoard(Turtle):

    score: int

    def __init__(self) -> None:
        super().__init__()
        self.pu()
        self.color("white")
        self.goto(0, 280)
        self.hideturtle()
        self.score = 0
        self.display_score()

    def display_score(self) -> None:
        self.write(f"Score: {self.score}", move=False, align='center',
                   font=('Arial', 10, 'normal'))

    def update(self) -> None:
        self.score += 1
        self.clear()
        self.display_score()

    def game_over(self) -> None:
        self.clear()
        self.display_score()
        self.goto(0,0)
        self.write("Game Over", move=False, align='center',
                   font=('Arial', 10, 'normal'))
