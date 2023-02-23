class Topten:
    def __init__(self) -> None:
        self.num = 1
   
    ### give me object
    def __iter__(self):
        return self

    #next value

    def __next__(self):
        if self.num <=10:
            val =self.num
            self.num += 1

            return val
            
        else:
            raise StopIteration

#for loops used iter internally

values=Topten()
print(values.__next__())
print(values.__next__())
for i in values:
    print(i)