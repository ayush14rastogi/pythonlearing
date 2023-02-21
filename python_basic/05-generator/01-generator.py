'''Generator-Function: A generator-function is defined like a normal function, 
but whenever it needs to generate a value, it does so with the yield keyword rather than return. 
If the body of a def contains yield, the function automatically becomes a generator function. 
'''
# A simple generator for Fibonacci Numbers
def mygenerator():
    yield 5

# Create a generator object
value=mygenerator()
print(mygenerator().__next__())