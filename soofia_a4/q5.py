# 5. *Write a Python program to enter a number in and print its equivalent binary, octal and hex

num = int(input("enter a number"))

print("Binary representation of {} is {}".format(num,bin(num)))

print("Octal representation of {} is {}".format(num,oct(num)))

print("Hexadecimal representation of {} is {}".format(num,hex(num)))