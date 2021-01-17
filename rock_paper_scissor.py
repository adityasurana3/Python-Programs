import random

def game(a ,b):
    if a == b:
        return None
    elif a == 'r':
        if b == 's':
            return False
        elif b=='p':
            return True
    elif a =='p':
        if b =="r":
            return False
        elif b =="s":
            return True
    elif a =="s":
        if b =='r':
            return False
        elif b =='p':
            return True 
print("Welcome to Rock paper Scissor game ")
comp = print("Comp: rock(r), paper(p), scissor(s)")
randNo = random.randint(1,3)


if randNo==1:
    comp ="r" or "rock"
elif randNo ==2:
    comp="p" or "paper"
elif randNo ==3:
    comp=="s" or "Scissor"
print("Choose between r,s,p")
you = input("your turn: rock(r), paper(p),Scissor(r): ")
a = game(comp,you)
print(f"Comp choose: {comp}")
print(f"You choose : {you}")
if a ==None:
    print("The match is tie")
elif a:
    print("You win")
else:
    print("You lose")