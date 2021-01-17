def greatest(a,b,c):
    if a>b and a>c:
        print("A is grester")
    elif b>a and b>c:
        print("B is greater")
    else:
        print("C is greater")

n1 = int(input("Enter A"))
n2 = int(input("Enter B"))
n3 = int(input("Enter C"))
greatest(9,11,16)