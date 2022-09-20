# 5. *Write a Python program to enter a number in and print its equivalent binary, octal and hexa
n = int(input("enter a number"))
print("Binary representation of {} is {}".format(n,bin(n)))
print("Octal representation of {} is {}".format(n,oct(n)))
print("HexaDecimal representation of {} is {}".format(n,hex(n)))