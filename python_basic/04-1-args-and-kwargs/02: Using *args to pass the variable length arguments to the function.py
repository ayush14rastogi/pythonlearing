#take non-keyword argument or unamed argument.

def adder(*arg):
    for count, thing in enumerate(arg):
        print('{0}. {1}'.format(count, thing))

adder('apple','banana')
#adder(4,5,6,7)
#adder(1,2,3,5,6)

