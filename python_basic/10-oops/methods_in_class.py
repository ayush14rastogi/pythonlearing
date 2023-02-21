import os 
os.system('clear')
class Student:

    school ="Bal Bharti public school"

    #constructor
    def __init__(self,m1,m2,m3) -> None:
        #instance variable
        self.m1=m1
        self.m2=m2
        self.m3=m3
    
    #instance method
    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    @classmethod
    def getSchool(cls) -> None:
        return cls.school
    
    @staticmethod
    def info():
        return "This is from static methods"


s1=Student(32,44,35)
s2=Student(43,44,27)

print("This is using instance methods :",s1.avg())
print("This is using classmethod methods :", Student.getSchool())
print("This is using classmethod methods :", Student.info())