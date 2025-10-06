# PROBLEM STATEMENT 
""" Print a diamond using * """

def Diamond(N):
    
    for x in range(1, N+1):
        
        for y in range(N - x):
            print(" ", end="")
        
        for z in range(1,2*x):
            print("*", end="")
        print()

    for x in range(N, 0, -1):
        
        for y in range(N - x):
            print(" ", end="")
        
        for z in range(1,2*x):
            print("*", end="")
        print()

Diamond(5)
        
        



    