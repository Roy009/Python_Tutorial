def greet(name, message):
    print("Hey", name,message)


def greetings(name, message):
    s = f"Hi there, {name} this side,{message}"
    print(s)

def sum(num1, num2):
    sumOfNum = num1 + num2
    return sumOfNum
def avg(sum, num):
    result = sum / num
    return result

# calling the function
greet("Rohit", "Good Morning")
greetings("Rohit", "Good Morning")
sum(23,65)
avg(789,3)