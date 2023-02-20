import os
os.system("clear")
print("hello below is the output")

def outer(a,b):
    print(a/b)

def smart_div(func):
    
    #same paramaeter as taken by div i.e. a & b,
    def inner(a,b):
        if a<b:
            a,b=b,a
        #return the function which we are accepting
        return func(a,b)

    #return inner function
    return inner

div=smart_div(outer)
div(10,5)