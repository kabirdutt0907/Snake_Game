from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.color("white")
        self.penup()
        self.goto(0, 268)
        self.write(f"Score: {self.score} | High Score : {self.highscore}" ,align="center" , font=("Courier" , 24 , "normal"))
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score : {self.highscore}", align="center", font=("Courier", 24, "normal"))


    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


    def Game_Over(self):
        self.goto(0 , 0)
        self.color("Red")
        self.write("Game Over due to Wall Collision" , align="center" , font=("Courier" , 20 , "normal"))

    def Game_Over1(self):
        self.goto(0 , 0)
        self.color("Red")
        self.write("Game Over due to Tail Collision" , align="center" , font=("Courier" , 20 , "normal"))