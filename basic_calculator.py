operator = input("Enter an operator(+ - * /): ")
num1 = float(input("num1 > num2 \nEnter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if operator == "+":
    result = num1 + num2
    print(result)

elif operator == "-":
    result = num1 - num2
    print(result)

elif operator == "*":
    result = num1*num2
    print(round(result, 2))

elif operator == "/":
    result = num1/num2 
    print(round(result, 2))

else:
    print(f"The Operator {operator} is NOT VALID")