# PROBLEM STATEMENT 
""" Find the Fibonacci Sequence of n terms """

n = int(input("Enter the no.of Fibonacci terms to be displayed: "))

Fib_List = [0,1]
Holder_Fib_next = 0

if n == 1:
    print(0)

elif n == 2:
    print(1)

elif n > 2:
    
    for i in range(2,n):
        Holder_Fib_next = Fib_List[i-2] + Fib_List[i-1]
        Fib_List.append(Holder_Fib_next)
    
    print(*Fib_List)  # * : it is the unpacking operator used before lists to remove the commas and brackets and print just the elements
        

# Efficent Version 
n = int(input("Enter the number of Fibonacci terms: "))

a, b = 0, 1

if n <= 0:
    print("Please enter a positive integer.")

elif n == 1:
    print(a)

else:
    print(a, b, end=" ")
    for _ in range(2, n):
        a, b = b, a + b
        print(b, end=" ")
        

