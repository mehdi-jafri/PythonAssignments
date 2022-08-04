fruits = ["Apple", "Mango","Banana","Cherry","stawberry","grapes","kiwi"]
string = str(input("enter fruits name to check"))
if string in fruits:
    i = fruits.index(string)
    print("item found at position ", i)
else:
    print("item not found")
print(fruits)