def remove(string,word):
    newStr= string.replace(word,"")
    return newStr.strip()

this = "   Hello There Everyone   "
print(this.strip())
n=remove(this,"Hello")
print(n)