import os
os.system("clear")
print("hello below is the output")

'''
https://www.programiz.com/python-programming/decorator
Pass Function as Argument, We can pass a function as an 
argument to another function in Python. For Example,
'''
def add(x, y):
    return x + y

def calculate(func, x, y):
    return func(x, y)

result = calculate(add, 4, 6)
print(result)  # prints 10