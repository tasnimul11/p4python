'''This Basic Calculator v2 does not take input unless a valid operator
    also it asks for another input if any Invalid operator is pressed
'''

while True:
    operator = input("Enter an operator(+ - * /): ")
    
    # Check if operator is valid before proceeding
    if operator in ['+', '-', '*', '/']:
        # Only ask for numbers if operator is valid
        num1 = float(input("num1 > num2 \nEnter the 1st number: "))
        num2 = float(input("Enter the 2nd number: "))

        if operator == "+":
            result = num1 + num2
            print(result)
        elif operator == "-":
            result = num1 - num2
            print(result)
        elif operator == "*":
            result = num1 * num2
            print(round(result, 2))
        elif operator == "/":
            result = num1 / num2 
            print(round(result, 2))
        break  # Exit the loop(here while loop) after successful calculation
        
    else:
        print(f"The Operator {operator} is NOT VALID")
        print("Please Try Again with a valid operator")
        continue  # Ask for operator again

'''Key changes made:
-Added a while True loop to keep asking for input until valid
-Moved the operator validation before number inputs
-Only asks for numbers if the operator is valid
-Added option to try again if invalid operator is entered'''