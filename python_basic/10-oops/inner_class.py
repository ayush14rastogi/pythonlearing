import os 
os.system('clear')

class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno

    def show(self):
        print(self.name, self.rollno)

s1=Student('Ayush',2)
s2=Student('sunny',2)

#print(s1.name,s1.rollno)  
#print(s2.name,s2.rollno)  

s1.show()