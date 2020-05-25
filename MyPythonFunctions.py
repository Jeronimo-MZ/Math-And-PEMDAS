from random import randint
from os import rename, remove

class MathGame:
    def __init__(self):
        self.user_name = ""
        self.operand_list = [0, 0, 0, 0, 0]
        self.operator_list = []
        self.operator_dict = {1: '+', 2: '-', 3: '*', 4: '**'}

    def get_user_name(self):
        self.user_name = str(input("Enter your User Name: ").title())
    
    def get_score(self, user_name):
        try:
            file = open("scores.txt", "r")
            for line in file:
                content = line.split(",")
                if content[0] == self.user_name:
                    file.close()
                    return content[1]
            file.close()
            return "-1"
        except IOError:
            print("\n scores.txt not found. It will be created!")
            file = open("scores.txt", "w")
            file.close()
            return "-1"


starter = MathGame()
starter.get_score("User")
