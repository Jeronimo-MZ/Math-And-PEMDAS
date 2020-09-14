from random import randint
from UserManagement import User

class MathGame:
    def __init__(self):
        self.user_name = ""
        self.operand_list = [0, 0, 0, 0, 0]
        self.operator_list = []
        self.operator_dict = {1: '+', 2: '-', 3: '*', 4: '**'}
        self.question_string = ""
        self.final_score = 0

    def get_user_name(self):
        self.user_name = str(input("Enter your User Name: ")).title()
        return self.user_name

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

    def Iniciar(self):
        usuario = User()
        user_name = self.get_user_name()
        temp = usuario.search(userName=user_name)

        if temp is None:
            usuario.addUser(user_name)
        del temp

        score  = usuario.getScore(user_name)
        user_choice = ''
        while user_choice != "N":
            self.get_answer()
            score = score + self.compare()
            while user_choice != "N":
                user_choice = input("Insert [Y] to continue or [N] to finish: ").upper()
                if user_choice == "Y":
                    break
                elif user_choice != "N":
                    print("Please Insert [Y] or [N]")
        usuario.updateScore(score)
        self.final_score = score
        usuario.close()

    def show_score(self):
        print(f"Your Final score was {self.final_score}")

