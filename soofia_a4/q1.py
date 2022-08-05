# 1. Write a python program to do the following on fruits list
# Fruits = [‘Apple’,’Banana’,’Mango’,’Cherry’, ‘Muskmelon’]

import random


Fruits = ["Apple","Banana","Mango","Cherry", "Muskmelon"]
print(Fruits)

# a. *Add watermelon
Fruits.append("watermelon")
print(Fruits)


# b. *Sort fruits
Fruits.sort()
print(Fruits)

# c. *Remove Cherry
Fruits.remove("Cherry")
print(Fruits)

#  d. *Count fruits
print(len(Fruits))

# e. *Print Banana and Mango
print(Fruits[1:3])

# f. *Print only 2 & 3 rd element
print(Fruits[1:3])

# g. ! Print random fruit name
x = random.choice(Fruits)
print(x)