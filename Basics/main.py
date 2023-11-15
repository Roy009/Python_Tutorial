# Operators

num1 = 10
num2 = 12

# Arithmetic Operators
print("-----Arithmetic-----")
print("num1 + num2 is ", num1 + num2)
print("num1 - num2 is ", num1 - num2)
print("num1 * num2 is ", num1 * num2)
print("num1 / num2 is ", num1 / num2)
print("num1 ** num2 is ", num1 ** num2)
print("num1 // num2 is ", num1 // num2)
print("num1 % num2 is ", num1 % num2)
print("-----X-----")

# Assignment Operators
print("-----Assignment-----")
a = 10
a += 10
print(a)
a -= 10
print(a)
a *= 10
print(a)
a /= 10
print(a)
print("-----X-----")
# Comparison Operators
x = 10
y = 11
print("-----Comparison-----")
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
print(x == y)
print("-----X-----")

print("-----Logical-----")
print(x == y and x > y)
print(x < y or x > y)
print(not(False))
print(not(True))
print("-----X-----")


# Control Statements
print("Control statements")
age = int(input("Enter your age: "))

if(age >= 18):
    print("Yes you can drive")
else:
    print("No you cannot drive")

# match case
print("Match case")
match a:
    case 1:
        print("Case is 1")
    case 2:
        print("Case is 2")
    case 3:
        print("Case is 3")
    case 4:
        print("Case is 4")
    case 5:
        print("Case is 5")
    case _:
        print("Case is 1")

# Loops

# for loop
print("For loop")
for i in range(5):
    print(i+1)
# for loop for list set
list1 = [1, 2, 3, 4, 5, 6]
for item in list1:
    print(item)
# while loop
print("while loop")
while(i < 10):
    print(i)
    i+=1