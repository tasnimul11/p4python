#MATH
import math

print(math.pi)  #pi value
print(math.e)   # e value

a = 9
b = 5.3

result = math.sqrt(9) #square root
print(result)

result = math.ceil(b) #rounds value up
print(result)

result = math.floor(b)  #rounds value down
print(result)

result = pow(a, 2)  #a^2
print(result)

result = pow(b, 3)  #b^3
print(result)

#------------------------------
#-----Possible without importing math library-----
print("without importing math library")
x = 3.1416
y = -4
z = 5

rounding_value = round(x)
abs_value = abs(y)
max_value = max(x, y, z)
min_value = min(x, y, z)

print(rounding_value)
print(abs_value)

print(max_value)
print(min_value)
