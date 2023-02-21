import os
 
# Clearing the Screen
os.system('clear')

class Computer:

    def __init__(self) -> None:
        self.name = "Navin"
        self.age = 28 
    
    def compare(self,other):
        if self.name == other.name or self.age == other.age:
            return True
        else:
            return False
c1=Computer()
c2=Computer()

print("Name of C1 is before changing", c1.name)
##change the value of c1 object
c1.name = "Ayush"
#c1.age = 30
if c1.compare(c2):
    print("they are same")

else:
    print("they are different")


print("Name of C1 is After changing", c1.name)
print("Name of C1 is After changing", c2.name)
