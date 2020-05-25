from random import randint
from os import rename, remove

class MathGame:
    def __init__(self):
        self.user_name = ""
        self.operand_list = [0, 0, 0, 0, 0]
        self.operator_list = []
        self.operator_dict = {1: '+', 2: '-', 3: '*', 4: '**'}
        self.question_string = ""

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

    def generate_question(self):
        while True:
            for c in range(5):
                self.operand_list[c] = randint(1,9)
            for c in range(4):
                if c > 0 and self.operator_list[c-1] != "**":
                    operator = self.operator_dict[randint(1, 4)] 
                else:
                    operator = self.operator_dict[randint(1, 3)]
                self.operator_list.append(operator)
            self.question_string = f"{self.operand_list[0]}{self.operator_list[0]}{self.operand_list[1]}"\
                f"{self.operator_list[1]}{self.operand_list[2]}{self.operator_list[2]}{self.operand_list[3]}{self.operator_list[3]}{self.operand_list[4]}"
            result = eval(self.question_string)
            if -50000 <= result <= 50000:
                break
        self.question_string = self.question_string.replace("**", "^")
        self.question_string = self.question_string.replace("*", "x")
        return self.question_string



starter = MathGame()
question = starter.generate_question()
print(question)
