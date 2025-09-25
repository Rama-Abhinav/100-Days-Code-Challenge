# PROBLEM STATEMENT 
""" Finding all the divisors of a given number  """

Number = input("Enter Number: ")

for i in range(1,(int(Number)+1)):
    if int(Number)%i == 0:
        print(i , end = " ")
        
        
    
