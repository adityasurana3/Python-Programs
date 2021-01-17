def natural(n):
    
    if n==0 or n==1:
        return 1
    else:
        return n + natural(n-1)

sum= natural(5)
print(sum)
