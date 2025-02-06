#conditional expression is a one-line shortcut of the if-else statement (ternary operator)
#Does not ask continuously
num = int(input("Enter a number to check if it is even or odd: "))
#can also write like below
#print(f"{num} is EVEN" if num % 2 == 0 else f"{num} is ODD")

print("Even" if num%2 == 0 else "ODD")

#Asks continuously
'''
while True:
    num = int(input("Enter a number to check if it is even or odd: "))
    print("Even" if num%2 == 0 else "ODD")
    #can also write like below
    #print(f"{num} is EVEN" if num % 2 == 0 else f"{num} is ODD")
    continue    #to continue asking
'''

   
#----Find Positive or Negative---------
num = float(input("Check whether it is POSITIVE or NEGATIVE: "))
print("POSITIVE" if num > 0 else "NEGATIVE")

#-----Find Max/Min------
print("Find Maximum and Minimum")
a = float(input("Enter 1st value: "))
b = float(input("Enter 2nd value: "))

max_num = a if a > b else b
min_num = a if a < b else b
print(f"Maximum = {max_num}")
print(f"Minimum = {min_num}" )

#-----Age Status----
age = int(input("Enter your Age: "))
status = "Adult" if age > 18 else "Child"
print(status)

#--------Weather-------

temp = int(input("Enter the Temperature today: "))
weather = "HOT" if temp > 22 else "COLD"
# we may use or/and operators as well (like below)
#weather = "COLD" if temp < 22 or temp < -11 else "HOT"
print(weather)

#-----Password/Access------

user_pass = input("Enter Password: ")
access_level = "Logged In" if user_pass == "admin123" else "Wrong Password"
print(access_level)
