#fruit list2 and add the new list in existing

#using extend method
a=["apple","banana"]
b=['orange','kiwi']

a.extend(b)
print(a)

#usin append method

s1=["orange","banana"]
s2=["greenapple","kiwi"]
s1.append(s2)
print(s1)


#for set

a1={'orange','banana'}
a2={'papaya'}
a1 |= a2
print(a1)

b1={'orange','banana'}
b2={'papaya',"lolo"}
b1.update(b2)
print(b1)


b1={'orange','banana'}
b2={'papaya',"lolo","nana","jaja"}
b1.union(b2)
print(b1)
