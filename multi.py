n = int(input("Enter the number"))
# Method 1
# for i in range(10,0,-1): 
# Method 2
for i in reversed(range(11)): 
    table=n*i
    print(n,"*", i, "=",table)