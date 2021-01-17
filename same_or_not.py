file1="sample.txt"
file2="this.txt"
with open(file1,'r') as f:
    f1=f.read()
with open(file2,'r') as f:
    f2=f.read()

if f1==f2:
    print("same")
else:
    print("Not same")
    
