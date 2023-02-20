
class Computer:
    def conf(self):
        print("i5,16gb,1TB")


com1=Computer()
com2=Computer()
print(type(com1))
Computer.conf(com1)
Computer.conf(com2)

com1.conf()
com2.conf()
a=5
a.bit_length()
print(a)