with open("sample.txt","r") as f:
    a=f.read()
with open("this.txt","w") as f:
    f.write(a)