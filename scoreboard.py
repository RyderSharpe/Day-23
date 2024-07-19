from turtle import Turtle

FONT = ("Courier", 20, "normal")
game_over_font = ("Courier", 35, "bold")
game_over = "Game Over Loser"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.hideturtle()  # Hide the turtle object
        self.penup()
        self.update_score()


    def update_score(self):
        self.clear()
        self.goto(-310, 270)  # Set the position for the left player's score
        self.write(f" Score:{self.score}", align="left", font=FONT)


    def increase_score(self):
        self.score += 1

    def clear_score(self):
        self.clear()

    def game_over(self):
        self.goto(-200, 0)  # Set the position for the left player's score
        self.write(game_over, align="left", font=game_over_font)
