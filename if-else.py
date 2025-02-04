age = int(input("Enter your age: "))


'''if age >= 35:       
    print("Sorry, you are not eligible for applying")
'''
#using range() function
'''
if age in range(18, 36):
   print("You are good to go.")
'''

#without using range function
if age > 35:
    print("Sorry, you are not eligible for applying")
elif age > 18:
    print("You are good to apply >>")
elif age <= 0:
    print("You have not born yet.")
    
else:
    print("You must be between 18 and 35 to be eligible.")

