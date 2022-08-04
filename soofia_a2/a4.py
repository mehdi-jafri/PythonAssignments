# Write a Python program to ask user to enter item (fruit) to delete from the existing list,
# if item does not exist then display message that item not found.

fruits = ["apple","mango","orange"]

search_fruit = input("enter fruit to search")
i=0
c=0
for x in fruits:
    if search_fruit == x:
        c=0
        break
    else:
        c=c+1
    i = i+1


if(c==0):
    fruits.pop(i)
    print("after removing {} from fruits list, new list is: {}\n".format(search_fruit, fruits))
else:
    print("{} is not in the list".format(search_fruit))


# if search_fruit in fruits:
#     fruits.remove(search_fruit)
# else:
#     print("{} not in list".format(search_fruit))

# print(fruits)

