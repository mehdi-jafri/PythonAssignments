# 4. ! Write a program check palindrome number and String

def num_palin(num):
    n = num
    s = 0
    while(n>0):
        r = n%10
        s = 10*s+r
        n = n//10
    if(s == num):
        print("palindrome")
    else:
        print("not palindrome")

def str_palin(str):
    str2 = str[::-1]
    if str2 == str:
        print("palindrome string")
    else:
        print("not palindrome string")


num = int(input("enter a number to check palindrome"))
num_palin(num)

str = input("enter a string to check palindrome or not")
str_palin(str)