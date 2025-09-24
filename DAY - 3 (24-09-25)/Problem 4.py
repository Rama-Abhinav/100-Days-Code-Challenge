# PROBLEM STATEMENT 
""" Find the GCD and LCM Of Two Numbers """

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

Set_a = set()
Set_b = set()

for num_a in range(1,a+1):
    if a%num_a == 0:
        Set_a.add(num_a)

for num_b in range(1,b+1):
    if b%num_b == 0:
        Set_b.add(num_b)
        
Common_Factors = Set_a.intersection(Set_b)

GCD = max(Common_Factors)
LCM = int((a*b)/GCD)

print(f"\nFor the Numbers {a} and {b}\nGreatest Common Divisor = {GCD}\nLowest Common Multiple = {LCM}\n")

## Using Math Module 
import math 

print(math.gcd(a,b))

