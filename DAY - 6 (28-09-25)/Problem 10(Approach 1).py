# PROBLEM STATEMENT 
""" Printing Pascal's Triangle upto n rows"""

from math import factorial, fabs 

Rows = int(input("Enter no.of Rows Required: "))

for x in range(Rows):
    
    print(" "*(Rows-x), end=" ")                            # Formatting Rows
    
    for y in range(x+1):
            Denominator = factorial(y)*(factorial((x-y)))   
            nCi = factorial(x)/Denominator
            print(int(nCi), end=" ")
    print()                                                 # Prints New Line            
    

