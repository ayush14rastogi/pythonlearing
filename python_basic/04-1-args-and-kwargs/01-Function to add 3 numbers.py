def adder(x,y,z):
    print(" sum:",x+y+z)

print("output from adder : ", end=',')
adder(10,12,13)

print("output from newadder : " )

def new_adder(x,y,z):
    print("sum:",x+y+z)

try:
    new_adder(5,10,15,20,25)
except Exception as e: print(e)