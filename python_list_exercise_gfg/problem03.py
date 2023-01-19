#Python – Swap elements in String list

test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']

print("The original list is : " + str(test_list))
  
# from list to string conversion
res = ", ".join(test_list)
res = res.replace("G", "A").replace("i","B").split(",")
 
print(res)
