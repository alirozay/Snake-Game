from turtle import Turtle
from datetime import datetime, timezone


class ScoreBoard(Turtle):

    score: int
    high_score: int

    def __init__(self) -> None:
        super().__init__()
        self.pu()
        self.color("white")
        self.goto(0, 280)
        self.hideturtle()
        self.score = 0
        self.get_scores()
        self.display_score()

    def get_scores(self) -> None:
        with open("high_score.txt", mode="r") as f:
            scores = f.readlines()
            if len(scores) == 2:
                print("H")
                self.high_score = int(scores[-1])
            else:
                self.high_score = int(scores[-1][-1])

    def display_score(self) -> None:
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",
                   move=False, align='center',
                   font=('Arial', 10, 'normal'))

    def update(self) -> None:
        self.score += 1
        self.display_score()

    def reset(self) -> None:
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_scores()
        self.score = 0
        self.display_score()

    def write_scores(self) -> None:
        with open("high_score.txt", mode="a") as f:
            result = "\n" + str(datetime.now(timezone.utc))
            result += f" {self.high_score}"
            f.write(result)

    # def game_over(self) -> None:
    #     self.clear()
    #     self.display_score()
    #     self.goto(0,0)
    #     self.write("Game Over", move=False, align='center',
    #                font=('Arial', 10, 'normal'))
