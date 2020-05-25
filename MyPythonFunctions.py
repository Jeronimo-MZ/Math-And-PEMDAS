from random import randint
from os import rename, remove

class MathGame:
    def __init__(self):
        self.user_name = ""

    def get_user_name(self):
        self.user_name = str(input("Enter your User Name: ").title())
    
    def get_score(self, user_name):
        file = open("scores.txt", "r")
        for line in file:
            content = line.split(",")
            print(content)
        file.close()


starter = MathGame()
starter.get_score("User")
