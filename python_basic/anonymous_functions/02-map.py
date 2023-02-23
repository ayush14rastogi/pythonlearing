nums=[1,2,3,4]

even=list(filter(lambda n:n%2,nums))
doubles =list(map(lambda n:n*2, even))

print(even)
print(doubles)