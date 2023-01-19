#Python program to swap two elements in a list
def swappositions(mylist, pos1, pos2):

    first = mylist.pop(pos1)
    second = mylist.pop(pos2-1)

    mylist.insert(pos1,second)
    mylist.insert(pos2,first)

    return list

list=['10','22','44','15','56']
pos_x=2
pos_y=4
print("original list : ", list)
print(("swap postion between {0} and {1} index.").format(pos_x, pos_y))
print("list after swap:", swappositions(list, pos_x, pos_y))