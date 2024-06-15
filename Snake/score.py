from turtle import Turtle

ALLIGN = "center"
FONT = ("Courier", 20, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(
            "data.txt",
            mode="r",
        ) as data:
            self.highscore = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.pendown()
        self.write(
            f"Score: {self.score} High Score: {self.highscore}",
            False,
            align=ALLIGN,
            font=FONT,
        )

    def score_update(self):
        self.clear()
        self.score += 1
        self.write(
            f"Score: {self.score} High Score: {self.highscore}",
            False,
            align=ALLIGN,
            font=FONT,
        )

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open(
                "data.txt",
                mode="w",
            ) as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.highscore}",
            False,
            align=ALLIGN,
            font=FONT,
        )
