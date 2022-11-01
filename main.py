# Program make a simple calculator
import Calculation as c

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide") 


while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")
    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", c.add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", c.subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", c.multiply(num1, num2))
            
        elif choice =='4':
            if num2 == 0:
                print("Don't put a zero in the denominator")
                continue
            else:
                print(num1, "/", num2, "=", c.divide(num1,num2))
            

        # check if user wants another calculation
        # break the while loop if answer is no
        while True:
            next_calculation = input("Let's do next calculation? (yes/no): ")
            # Change to Lowercase to Troubleshoot
            next_calculation = next_calculation.lower()
            if next_calculation == "no":
                while True:
                    True_exit = input("Are you sure? (yes/no): ")
                    True_exit = True_exit.lower()
                    if True_exit == "yes":
                        break
                    elif True_exit == "no":
                        break
                    else:
                        continue                   
                break
            elif next_calculation == "yes":
                break
            else:
                continue

        if True_exit == "yes" and next_calculation == "no":
            break
            

    else:
        print("Invalid Input")
