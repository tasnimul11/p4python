friends = int(input("How many friends do you have? : "))

friends = friends + 1
friends += 1    #augmented assignment operator

friends = friends - 2
friends -= 2

friends = friends * 3
friends *= 3

friends = friends / 2
friends /= 2

friends = friends ** 2 #exponential operator ** here's SQUARED
friends **= 2

print(friends) 

#Modulus operator % gives remainder

friends = int(input("How many friends in in total in 3 groups?: "))

remainder = friends % 3
x = round(remainder)

print(f"{x} friend(s) remain without a group.")


