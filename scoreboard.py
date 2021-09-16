from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 268)
        self.write(f"Score: {self.score}" ,align="center" , font=("Courier" , 24 , "normal"))
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))

    def Game_Over(self):
        self.goto(0 , 0)
        self.color("Red")
        self.write("Game Over due to Wall Collision" , align="center" , font=("Courier" , 20 , "normal"))

    def Game_Over1(self):
        self.goto(0 , 0)
        self.color("Red")
        self.write("Game Over due to Tail Collision" , align="center" , font=("Courier" , 20 , "normal"))