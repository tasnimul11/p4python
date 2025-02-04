response = input("Are you married? (Y/N): ")

if response == "Y":
    name = input("What's your name?")
    if name == "":
        print("You have NOT entered any.")
    else:
        print(f"Hi, {name}. Have a good day with your spouse.")
        print("You have 2 gifts, one you for you, one for your Spouse!!")

elif response == "N":
    print("Ahha, single! Have a gift, enjoy!!")
    
else:
    print("Wrong Input!!")

#taking one's name
'''
name = input("What's your name?")
if name == "":
    print("You have NOT entered any.")
else:
    print(f"Hi, {name}. Have a good day with your spouse.")
'''

#