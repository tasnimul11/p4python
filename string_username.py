#1 username must not exceed 7 characters
#2 username must not contain any space
#3 username must not contain any digit

username = input("Create your username: ")

if len(username) > 7:
    print("Your username must not exceed 7 characters")
elif not username.find(" ") == -1: #if it does NOT find(not) "space is NOT found(-1)"
    print("Your username must not contain any space")
elif not username.isalpha(): #if it does not have "only alphabetic input"
    print("Your username must not contain any Digit")

print(f"Hi there, {username}")

#methods used: len(), .find(), .isalpha()