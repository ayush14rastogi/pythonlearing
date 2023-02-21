def decor1(func):
    def inner():
        x = func()
        print("from decor1 ",x*x)
        return x * x
    return inner
 
def decor(func):
    def inner():
        x = func()
        print("from decor ",2*x)
        return 2 * x
    return inner
 
@decor1
@decor
def num():
    return 10
 
print(num())