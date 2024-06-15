from turtle import Turtle

ALLIGN = "center"
FONT = ("Courier", 20, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.pendown()
        self.write(
            f"{self.l_score}      {self.r_score}", False, align=ALLIGN, font=FONT
        )

    def l_score_update(self):
        self.clear()
        self.l_score += 1
        self.write(
            f"{self.l_score}      {self.r_score}", False, align=ALLIGN, font=FONT
        )

    def r_score_update(self):
        self.clear()
        self.r_score += 1
        self.write(
            f"{self.l_score}      {self.r_score}", False, align=ALLIGN, font=FONT
        )

    def game_over(self):
        if self.l_score == 11:
            self.penup()
            self.goto(20, 0)
            self.pendown()
            self.write("Game Over.", False, align=ALLIGN, font=FONT)
            self.penup()
            self.goto(-100, -150)
            self.pendown()
            self.write("Left Player Won.", False, align="left", font=FONT)
            return True
        if self.r_score == 11:
            self.penup()
            self.goto(20, 0)
            self.pendown()
            self.write("Game Over.", False, align=ALLIGN, font=FONT)
            self.penup()
            self.goto(100, -150)
            self.pendown()
            self.write("Right Player Won.", False, align="right", font=FONT)
            return True
