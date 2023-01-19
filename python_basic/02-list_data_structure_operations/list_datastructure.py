mylist= []
print("Blank List: ", mylist)

print("Creating a list of numbers ---->", )
mylist= [10,20,14]
print("List of numbers: ", mylist)


# list methods
#append()	Adds an element at the end of the list

print("\nAppending a number '12' to mylist with append() method.")
mylist.append('12')
print("mylist after appending: ",mylist)

#https://stackoverflow.com/questions/2612802/how-do-i-clone-a-list-so-that-it-doesnt-change-unexpectedly-after-assignment
#copy()	Returns a copy of the list
print("\nCopying mylist to new list with clear() method.")
#newlist=mylist.copy()
newlist=mylist[::]
print("mylist is  :", mylist)
print("newlist is :", newlist)

#clear()	Removes all the elements from the list
print("\nClearing newlist with clear() method.")
newlist.clear()
print("newlist is :", newlist)
print("mylist is  :", mylist)


#count()	Returns the number of elements with the specified value
print("\nCounting newlist and mylist with count() method.")
print("mylist is :",mylist)
print("count of 10 is in list is:" ,mylist.count(10))


#extend()	Add the elements of a list (or any iterable), to the end of the current list
print("\nAdd the elements of a list (prime_numbers), to the end of the current list(numbers).")
prime_numbers = [2, 3, 5]
numbers = [1, 4]
print("prime_numbers list is: ",prime_numbers)
print("numbers list is: ",numbers)
numbers.extend(prime_numbers)
print('List after extend():', numbers)

#index()	Returns the index of the first element with the specified value
print("\nIndex of 4 is in numbers list using index() method",numbers.index(4))

#insert()	Adds an element at the specified position
numbers.insert(0,20)
print("\nInsert an element 10 at 0 index in numbers list using insert() method",numbers )

#pop()	Removes the element at the specified position
numbers.pop(0)
print("\npoping an element 10 from numbers list using pop() method", numbers)

#remove()	Removes the first item with the specified value
numbers.remove(5)
print("\nremoving an element 5 from numbers list using remove() method", numbers)


#reverse()	Reverses the order of the list
numbers.reverse()
print("\nrevering the numbers list using reverse() method", numbers)


#sort()	Sorts the list
numbers.sort()
print("\nsorting the numbers list using sort() method", numbers)
