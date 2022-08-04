fruits = ("Apple", "Mango", "Banana", "Cherry","stawberry","grapes")
tup2 = ()
tup3 = ()
i = 0
while i < len(fruits):
    if i % 2 == 0:
        tup2 += (fruits[i],)
    else:
        tup3 += (fruits[i],)
    i += 1
print(tup2)
print(tup3)

# or below code

print(fruits[::2])
print(fruits[1::2])