'''
As mentioned earlier, A Python decorator is a function that takes 
in a function and returns it by adding some functionality.
'''
#nested function
def make_pretty(func):
    # define the inner function 
    def inner():
       #add some additional behavior to decorated function
        print("I got decorated")
        func()
    return inner


#simple function
def ordinary():
    print("I am ordinary")

# decorate the ordinary function
decorated_func = make_pretty(ordinary)

# call the decorated function
decorated_func()
