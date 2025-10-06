# PROBLEM STATEMENT 
""" Print Mutliplication Table for any number """

def Tables(n):
    
    for y in range(1, 101):
        print(f"{y} x {n} = {(y*n)}")
            
Number = int(input("Enter Number to print its table: "))
Tables(Number)