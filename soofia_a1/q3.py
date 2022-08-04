#write a program to enter name phone and email and display

import email


name = input("enter your name: ")

#number is taken as string because len() is a method of string
number = input('Please enter your 10 digit number: ')

while len(number) != 10:
    number = input('That was not a 10 digit number. Please enter your 10 digit number ')

email_id = input("enter your email")

#displaying result
print("Your details are: \n Name: {}\n Phone: {} \n Email: {} ".format(name, number, email_id))
