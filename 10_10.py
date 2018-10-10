import random

a = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def board():
    print(a[0], "|", a[1], "|", a[2])
    print(a[3], "|", a[4], "|", a[5])
    print(a[6], "|", a[7], "|", a[8])

def isFree(myPos):
    if a[myPos] != "x" and a[myPos] != "#":
        return True
    else:
        return False

def gameResult():
    if a[0] == "x" and a[1] == "x" and a[2] == "x":
        return True
    elif a[3] == "x" and a[4] == "x" and a[5] == "x":
        return True
    elif a[6] == "x" and a[7] == "x" and a[8] == "x":
        return True
    elif a[0] == "x" and a[3] == "x" and a[6] == "x":
        return True
    elif a[1] == "x" and a[4] == "x" and a[7] == "x":
        return True
    elif a[2] == "x" and a[5] == "x" and a[8] == "x":
        return True
    else:
        return False

board()

me = input("Choose your side: ")
if me == "x":
    comp = "#"
else:
    comp = "x"

while True:
    myPos = int(input("Choose your position: "))
    if isFree(myPos):
        a[myPos] = me

    compPos = 0
    while compPos not in a:
        compPos = random.randint(1, 8)

    if isFree(compPos):
        a[compPos] = comp
    board()

    if gameResult():
        print("Game over!")
        break




