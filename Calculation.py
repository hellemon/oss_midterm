import os
import datetime


if os.path.isfile("cal_log.txt"):
    cal_log = open('cal_log.txt', 'a')
else:
    cal_log = open('cal_log.txt', 'w')

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

#Need to define divide function.
def divide (x,y):
    return x/y

def choice_cal(choice, num1, num2):
    if choice == '1':
        result = add(num1, num2)
        print(num1, "+", num2, "=", result)
        print(str(datetime.datetime.now()),"\n"+"add_function" , num1, "+", num2, "=", result, file = cal_log)
        return result

    elif choice == '2':
        result = subtract(num1, num2)
        print(num1, "-", num2, "=", result )
        print(str(datetime.datetime.now()),"\n"+"subtract_function", num1, "-", num2, "=", result, file = cal_log)
        return result

    elif choice == '3':
        result = multiply(num1, num2)
        print(num1, "*", num2, "=", result)
        print(str(datetime.datetime.now()),"\n"+"multiply_function", num1, "*", num2, "=", result, file = cal_log)
        return result
            
    elif choice =='4':
        result = divide(num1,num2)
        print(num1, "/", num2, "=", result)
        print(str(datetime.datetime.now()),"\n"+"divide_function", num1, "/", num2, "=", result, file = cal_log)
        return result
            