from random import randint
from os import rename, remove

class MathGame:
    def __init__(self):
        self.user_name = ""
        self.operand_list = [0, 0, 0, 0, 0]
        self.operator_list = []
        self.operator_dict = {1: '+', 2: '-', 3: '*', 4: '**'}
        self.question_string = ""
        self.final_score = 0

    def get_user_name(self):
        self.user_name = str(input("Enter your User Name: ").title())
        return self.user_name
    
    def get_score(self, user_name):
        try:
            file = open("scores.txt", "r")
            for line in file:
                content = line.split(",")
                if content[0] == self.user_name:
                    file.close()
                    return int(content[1])
            file.close()
            return "-1"
        except IOError:
            print("scores.txt not found. It will be created!")
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
            self.result = eval(self.question_string)
            if -50000 <= self.result <= 50000:
                break
        self.question_string = self.question_string.replace("**", "^")
        self.question_string = self.question_string.replace("*", "x")
        return self.question_string

    def get_answer(self):
        print(f"Question:{self.generate_question()}")
        while True:
            try:
                self.answer = int(input("Write your answer: "))
                break
            except ValueError:
                print("Invalid Value, you didn't enter a number. Please Try Again.")
            
    def compare(self):
        if self.answer == self.result:
            print("You're so smart!")
            return 1
        else:
            print(f"Sorry, wrong answer! The correct answer is {self.result}.")
            return 0

    def update_scores(self,user_name,score, new_user):
        if new_user:
            file = open("scores.txt", "a")
            file.write(f"{user_name}, {score}\n")
            file.close()
        else:
            new_file = open("scores.tmp","w")
            file = open("scores.txt", "r")
            for line in file:
                content = line.split(",")
                if content[0] == user_name:
                    line = f"{content[0]}, {score}"
                new_file.write(f"{line}\n")
            new_file.close()
            file.close()
            remove("scores.txt")
            rename("scores.tmp", "scores.txt")

    def Iniciar(self):
        user_name = self.get_user_name()
        score  = self.get_score(user_name)
        if score == '-1':
            new_user = True
            score  = 0
        else:
            new_user = False
        user_choice = ""
        while user_choice != "N":
            self.get_answer()
            score = score + self.compare()
            while user_choice != "N":
                user_choice = input("Insert [Y] to continue or [N] to finish: ").upper()
                if user_choice == "Y":
                    break
                elif user_choice != "N":
                    print("Please Insert [Y] or [N]")
        self.update_scores(user_name, score, new_user)
        self.final_score = score

    def show_score(self):
        print(f"Your Final score was {self.final_score}")

