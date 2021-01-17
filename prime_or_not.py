print("Enter the number")
n = int(input())
prime = True
for i in range(2,n):
    if n %i==0 and n!=2:
        prime=False
        break
if prime:
    print("Prime number")
else:
    print("Not prime")