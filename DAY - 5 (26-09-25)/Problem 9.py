# PROBLEM STATEMENT 
""" Finding the sum of all digits of a number along with the no.of digits in the number"""

Number = input("Enter Number Whose Sum is to printed: ")
Digits_List = [int(x) for x in Number] 
print(f"\nSum of Digits of {Number} = {sum(Digits_List)}\nNo.of Digits in The Number {Number} = {len(Number)}")