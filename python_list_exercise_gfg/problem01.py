#Python program to interchange first and last elements in a list
def swapList(mylist):

    first=mylist.pop(0)
    last =mylist.pop(-1)

    mylist.insert(0,last)
    mylist.append(first)

    return list


list=['1','2','4','5','6']
print(swapList(list))