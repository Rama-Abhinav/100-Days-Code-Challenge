# PROBLEM STATEMENT 
""" Swap two variable without using a third or temp variable """

Num1 = int(input("Enter 1st Number:"))
Num2 = int(input("Enter 2nd Number:"))

C = Num1+Num2
Num1 = (C) - Num1
Num2 = (C) - Num2

print(f"Num1 = {Num1}")
print(f"Num2 = {Num2}")
