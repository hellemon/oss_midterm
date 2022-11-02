import os.path
import Calculation as c
import datetime



if os.path.isfile("cal_log.txt"):
    cal_log = open('cal_log.txt', 'a')
else:
    cal_log = open('cal_log.txt', 'w')
if os.path.isfile('error_log.txt'):
    error_log = open('error_log.txt', 'a')
else:
    error_log = open('error_log.txt', 'w')

def process_function():
    num1 = 0
    num2 = 0
    while True:
        # take input from the user
        select_operation()
        choice = input("Enter choice(1/2/3/4): ")
        # check if choice is one of the four options
        if choice in ('1', '2', '3', '4'):
            
            num1 = (input("Enter first number: "))
            if num1.isdigit == True:
                num1 = float(num1)
            else :
                print("you must input number!!")
                continue

            num2 = (input("Enter second number: "))
            if num2.isdigit == True:
                num2 = float(num2)
            else :
                print("you must input number!!")
                continue
            

            if choice == '4' and num2 == 0:
                print("Don't put a zero in the denominator")
                print("{}\nDon't put a zero in the denominator user input num1 = {}, num2 = {} ".format(datetime.datetime.now(),num1, num2), file=error_log)
                continue
            answer = c.choice_cal(choice, num1, num2)

            # check if user wants another calculation
            # break the while loop if answer is no
            next_calculation = ""
            True_exit = ""
            while True:
                next_calculation = input("Let's do next calculation? (yes/no): ")
                # Change to Lowercase to Troubleshoot
                next_calculation = next_calculation.lower()
                if next_calculation == "no":
                    True_exit = sure_function()
                    break
                elif next_calculation == "yes":
                    break
                else:
                    continue

            if True_exit == "yes" and next_calculation == "no":
                break
            
        else:
            print("Invalid Input")
            print("{}\nInvalid Input user input choice = {}".format(datetime.datetime.now(), choice),file = error_log)

            
def sure_function():
    while True:
        True_exit = input("Are you sure? (yes/no): ")
        True_exit = True_exit.lower()
        if True_exit == "yes":
            return "yes"
        elif True_exit == "no":
            return "no"
        else:
            continue                   

def select_operation():
    print("\nSelect operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide") 