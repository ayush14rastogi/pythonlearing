
import sys

#total arguments
n=len(sys.argv)
print("total argument passed:", n)

# Arguments passed
print("\nName of Python script:", sys.argv[0])

print("\nArguments passed:", end = " ")

for i in range(1,n):
    print(sys.argv[i],end=" ")

sum=0

for i in range(1,n):
    sum+=  int(sys.argv[i])

print("\n\nResults:", sum)
