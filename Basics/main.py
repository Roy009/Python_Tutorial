# Variables in python 
a = 1
str = 'Hello, World!'
f = 1.2
print("Integer: " , a)
print("String: " , str)
print("float: ", f)
print("Hello, World!")
print(type(a))
print(type(str))
print(type(f))

# Taking Input - By default input function takes input as a string
num = input("Enter the number: ")
print("The Number is ", num)
# To take specific input we can use of type casting
int_input = int(input("Integer input"))
float_input = float(input("Float input"))
print(type(int_input))
print(type(float_input))

# Taking multiple input
# using split method
x, y = input("Enter two values: ").split()
print("x -> ", x)
print("y -> ", y)
#using List comprehension
u, v = [int(u) for u in input("Enter two values: ").split()]
print("First number is: ", u)
print("Second number is: ",)