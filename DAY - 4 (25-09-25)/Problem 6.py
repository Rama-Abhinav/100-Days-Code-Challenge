# PROBLEM STATEMENT 
""" Checking if a given Number is an Armstrong Number """

Number_to_check = input("Enter the Number to be checked: ")

Number_List = [int(x) for x in Number_to_check]

Power = len(Number_List)

Sum_Check_Arm = int()

for i in range(Power):
    
    Power_Raised_to = (Number_List[i] ** Power)
    Sum_Check_Arm += Power_Raised_to

print(f"\n{Sum_Check_Arm} = {Number_to_check}")

if Sum_Check_Arm == int(Number_to_check):
    print(f" The Number {Number_to_check} is an Armstrong Number ")
else:
    print(f"The Number {Number_to_check} is not armstrong as \nthe sum of its digits each rasied to the power of no.of digits is {Sum_Check_Arm} ")