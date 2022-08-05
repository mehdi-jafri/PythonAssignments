# 6. Write a program to check number is even or odd using if else

a = int(input("enter num to check even or odd"))
if a%2 ==0:
    print("even")
else:
    print("odd")


# 7. Write a program to enter a number in Python and print its octal and hexadecimal equvilnt

num = int(input("enter number"))

#octal
print("Octal of {} is {}".format(num,oct(num)))


#hexa
print("Hexadecimal of {} is {}".format(num,hex(num)))