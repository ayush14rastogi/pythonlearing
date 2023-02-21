import os
os.system('clear')
class Car:
    # class static variable

    wheel=4
    def __init__(self) -> None:
        self.mil=10
        self.company="BMW"

c1=Car()
c2=Car()
Car.wheel=5
c1.mil=20
print(c1.mil,c1.company,c1.wheel)
print(c2.mil,c2.company,c2.wheel)
