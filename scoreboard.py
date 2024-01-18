from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(x=0, y=265)
        self.score_write(0)

    def score_write(self, score):
        self.clear()
        self.write(f"Score: {score}", False, align="center",font=('Arial', 20, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, align="center",font=('Arial', 20, 'normal'))