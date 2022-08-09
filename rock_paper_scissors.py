import random

def gameWin(comp,you):
    if comp == you:
        return None
    elif(comp=='R'):
        if you=='P':
            return True
        elif you=='S':
            return False
    elif(comp=='P'):
        if you=='S':
            return True
        elif you=='R':
            return False
    elif(comp=='S'):
        if you=='R':
            return True
        elif you=='P':
            return False





print("Computer either chooses Rock(R) paper(p) Scissors(s)")
you=input("Enter Either Rock(R) or Paper(P) or Scissors(S) \n")
randNo = random.randint(1,3)
if randNo == 1:
    comp='R'
elif randNo == 2:
    comp="P"
elif randNo == 3:
    comp="S"

print("computer choose ",comp )
print("You choose ",you)

a= gameWin(comp,you)
if a== None:
    print("The Game is a tie!")
elif a:
    print("You Win")
else:
    print("You Loose")
