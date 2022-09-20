import random
Fruits = ["apple", "banana", "Mango", "Cherry" , "Muskmelon"]
print(Fruits)
# add watermelon
Fruits.append("Watermelon")
print(Fruits)
# sort fruits
Fruits.sort()
print(Fruits)
# Remove Cherry
Fruits.remove("Cherry")
print(Fruits)
# Count fruits
print(len(Fruits))
#print banana and mango
print(Fruits[0::4])
# print 2 and 3
print(Fruits[1:3])
# random
x = random.choice(Fruits)
print(x)