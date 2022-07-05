f=["orange","papaya","banana","pineapple","grapes"]
print(f)

f.append("blah")
print(f)


s={"greenapple","mango","banana","apple","watermelon","muskmelon"}
s.add("kala")
print(s)

m=frozenset(s)
print(m)
m.append("kiwi")
