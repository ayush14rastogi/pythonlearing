# Python3 program to demonstrate global() function
  
# global variable
a = 5
  
def func():
    c = 10
    d = c + a
      
    # Calling globals()
    globals()['a'] = d
    print (d)
      
# Driver Code    
func()
print(a)