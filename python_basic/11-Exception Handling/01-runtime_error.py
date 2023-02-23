
#x = list(map(int, input("Enter a multiple value: ").split()))
#a,b = x[0],x[1]
a,b =10,0
print("given input is {} {}".format(a,b))
#print(type(a))
try:
    print(a/b)


except ZeroDivisionError:
    print("you can not divide by zero :")