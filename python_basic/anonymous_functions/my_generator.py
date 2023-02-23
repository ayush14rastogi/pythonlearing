#top 5 values

def Topten():
    yield 3
    yield 4
    yield 5


value=Topten()
print(value.__next__())
print(next(value))