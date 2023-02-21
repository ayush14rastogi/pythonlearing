'''function-->inner decorator-->outer will run first'''

def star(func):
    def inner(*args, **kwargs):
        print("*" * 15)
        func(*args, **kwargs)
        print("*" * 15)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 15)
        func(*args, **kwargs)
        print("%" * 15)
    return inner

#@star
#@percent

@star
@percent
def printer(msg):
    print(msg)
#printer = star(percent(printer))
printer("Hello")

