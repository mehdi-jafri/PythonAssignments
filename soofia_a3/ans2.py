# 2. Write a python program which uses existing modules (import) to check even/odd
# number, print specified series, add specified item to existing fruit list and print the fruit
# list

import check as ck

n = int(input("Enter number to check if it is even or odd : "))
ck.check_even_odd(n)

n = int(input("Enter number to print series upto that number : "))
ck.series(n)

fruit = ["apple", "mango"]
ck.add_list(fruit)


ck.even_odd(1,2,3,4,5,5,6,7,8)
    