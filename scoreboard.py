from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0,260)
        self.write(f"Score: {self.score}",align='center',font=("Courier",24,'bold'))
        self.hideturtle()
    def IncraseScore(self):
        self.score += 1
        self.write(f"Score: {self.score}",align='center',font=("Courier",24,'bold'))
    def Clear_Screen(self):
        self.clear()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=("Courier",24,'bold'))
