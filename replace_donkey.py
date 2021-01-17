with open("sample.txt","r") as f:
    a = f.read()


a=a.replace("donkey","##@$$%$")

with open("sample.txt","w") as f:
    a=f.write(a)
