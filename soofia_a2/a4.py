fruits = ["Apple", "Mango","Banana","Cherry","stawberry","grapes","kiwi"]
string = str(input("enter fruits name to delete"))
if string in fruits:
    fruits.remove(string)
    print("item deleted")
else:
    print("item not found")
print(fruits)