# PROBLEM STATEMENT 
""" Finding the Factorial of a given number """

Num = int(input("Enter number to Find its Factorial: \n"))

if Num < 0:
    print(" Factorial for Negative Integers are not Defined !! ")

elif Num == 0:
    print(" 0! = 1 ")
    
elif Num >= 1:
    
    Factorial = 1
    for n in range(1,Num+1):
        Factorial *= n
        
    print(f"{Factorial}\n")
    

# Using math module

import math 

try:
    
    print(math.factorial(Num))
    
except ValueError:
    
    print(" Factorial for Negative Integers are not Defined !! ")
    
    
        
    
    