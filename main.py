import os
import datetime

if os.path.isfile("cal_log.txt"):
    cal_log = open('cal_log.txt', 'a')
else:
    cal_log = open('cal_log.txt', 'w')
    
# Program make a simple calculator
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


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide") 


while True:
    # take input from the user
    choice = input("Enter choice(1/2/3): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
            print(str(datetime.datetime.now()),"\n"+"add_function" , num1, "+", num2, "=", add(num1, num2), file = cal_log)


        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
            print(str(datetime.datetime.now()),"\n"+"subtract_function", num1, "-", num2, "=", subtract(num1, num2), file = cal_log)

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
            print(str(datetime.datetime.now()),"\n"+"multiply_function", num1, "*", num2, "=", multiply(num1, num2), file = cal_log)

        elif choice =='4':
            print(num1, "/", num2, "=", divide(num1,num2))
            print(str(datetime.datetime.now()),"\n"+"divide_function", num1, "/", num2, "=", divide(num1,num2), file = cal_log)
         

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break

    else:
        print("Invalid Input")