def add(a, b): 
    return a + b

def subtract(a, b): 
    return a - b

def multiply(a, b): 
    return a * b

def divide(a, b): 
    return a / b

a = int(input("son1 ni kiriting:"))
amal = input("Amalni kiriting (+ , - , * , / ): ")
b = int(input("son2 ni kiriting:"))

if amal == '+':
    print(add(a,b))
if amal == '-':
    print(subtract(a,b))
if amal == '*':
    print(multiply(a,b))
if amal == '/':
    print(divide(a,b))





