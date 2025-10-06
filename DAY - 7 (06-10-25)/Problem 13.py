# PROBLEM STATEMENT 
""" Print all prime numbers in a given range """

import math 


Start = 1
Stop = 100

Prime = []

for x in range(Start, Stop+1):
    
    if x > 1:
        
        if x%2 == 0 and x > 2:
            continue
        
        if x == 2:
            Prime.append(x)
            
        Root = int(math.sqrt(x))
        for i in range(3, Root+1, 2):
            
            if x%i == 0:
                continue
            
        else:
            Prime.append(x)
Prime.remove(2)
                
print(Prime)
                
            
            
            
        
        
                