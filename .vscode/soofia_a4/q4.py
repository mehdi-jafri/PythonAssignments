def numbers(num): 
    #num=int(input("Enter a number:")) 
    temp=num 
    rev=0 
    while(num>0): 
     dig=num%10 
     rev=rev*10+dig 
     num=num//10 
    if(temp==rev): print("The number is palindrome!") 
    else: print("Not a palindrome!") 
    def strings(string): 
        #string=input(("Enter a string:")) 
        if(string==string[::-1]): 
            print("The string is a palindrome") 
        else: print("Not a palindrome") 
        check=int(input("What you want to check palindrome of?\n1. Number\n2. String\n")) 
        if check==1: 
            num=int(input("Enter Number : ")) 
            numbers(num) 
        elif check==2: 
            string=(input("Enter String : ")) 
            strings(string) 
        else: 
            print("not a valid input.")