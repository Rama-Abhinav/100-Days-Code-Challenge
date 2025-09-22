# PROBLEM STATEMENT 
""" Checking if a given Number is Prime """

import math

User_Num = int(input("Enter Number to be Checked :"))                   # Taking user input of number to be checked

if User_Num > 1:                                                        # Checking if given number is greater than 1 as all prime numbers are positive
    
    if User_Num%2 == 0 and User_Num > 2 :                               # Checking if given number is even and greater than 2 as the only even prime number is 2
        print("!! The Only Even Prime Number is 2 !!")
    
    elif User_Num == 2:                                           
        print(" 2 is prime!! ")
        
    else:
        
        Root = int(math.sqrt(User_Num))                                 # Calculating the root of the number to define check range of divisibilty 
        
        for Check in range(3,Root+1 ,2):                                 # Using a for loop to iterate through each divisiblity test from 3 to the Root of the given number.
            
                if User_Num % Check == 0:                               # Checking if the number given is divisible by any of the numbers in the above defined range.                
                    print("Not Prime !!")                               # If divisible printing that the given number is not prime
                    break           
        
        else:
            print(f" The number {User_Num} is a prime number \n")           # If the check of divisibility is passed then printing that the given number is a prime number and is divisible on by itself and 1.
        


## Modification to get prime numbers in a given range
import math

Num = list(range(101))   
           
for User_Num in Num:
    
    if User_Num > 1:
        
        if User_Num == 2:
            print(User_Num)
            
        elif User_Num%2 == 0 and User_Num > 2:
            continue
        
        else:
            
            Root = int(math.sqrt(User_Num))    
            
            for Check in range(3,Root+1,2):
                
                if User_Num%Check == 0:
                    break
            
            else:
                print(User_Num)  
        