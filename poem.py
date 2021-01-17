f = open("poem.txt", "r")
a = f.read()
if 'twinkle' in a:
    print("Present")
else:
    print("Not present")

