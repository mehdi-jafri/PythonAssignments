#Write a python program to sort, reverse, count items of list

fruits = ["mango", "apple", "strawberry", "orange"]
#sorting
fruits.sort()
print("sort: ", fruits)
#reverse
fruits.reverse()
print("reverse: ", fruits)
#count total items
print("Number of items in list is : ",len(fruits))


#sort and reverse function sorts and reverses the list and returns none instead of returning a new list
#so when used with print statement it will print None value
#print(fruits.reverse())  will give None as output.