from MyPythonClass import MathGame
from time import sleep
print('='*50)
print("Arithmetics game".center(50))
print("="*50)

starter = MathGame()
starter.Iniciar()
while True:
    question = input("Do you want to see your Score?[Y/N]").upper()
    if question == "Y":
        starter.show_score()
        break
    elif question == "N":
        break
    else:
        print('Invalid Value! please insert "Y" or "N":')
input("Press Any Key To Finish....")



print('='*50)
print("Finished!!!".center(50))
print("="*50)
sleep(2)
