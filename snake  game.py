import random
userpoint=0
computerpoint=0
noofchances=0
print("  snake  water gun \n ")
list1=["s","w","g"]
while  noofchances<10:

    print("No f chances left ", 10 - noofchances)
    a = input("s for snake \nw for water\ng for gun \n")

    b=random.choice(list1)

    if a=="s" and b=="w":
        print(f"Your choice is  {a} and computer choice is {b}" )
        userpoint=userpoint+1
        noofchances=noofchances+1
        print(userpoint)
        print("Winner")


    elif a=="s" and b=="s ":
        print(f"Your choice is  {a} and computer choice is {b}" )
        noofchances = noofchances + 1
        print("Tie ")
    elif a=="s" and b=="g":
        print(f"Your choice is  {a} and computer choice is {b}")
        computerpoint=computerpoint+1
        noofchances = noofchances + 1
        print(computerpoint)
        print("Your are loser ")
    elif a=="w" and b=="s":
        print(f"Your choice is  {a} and computer choice is {b}")
        computerpoint = computerpoint + 1
        noofchances = noofchances + 1
        print(computerpoint)
        print("Your are loser ")
    elif a=="w" and b=="w":
        print(f"Your choice is  {a} and computer choice is {b}")
        print("Tie ")
        noofchances = noofchances + 1
    elif a=="w" and b=="g":
        print(f"Your choice is  {a} and computer choice is {b}")
        userpoint = userpoint + 1
        print(userpoint)
        print("Winner")
    elif a=="g" and b=="s":
        print(f"Your choice is  {a} and computer choice is {b}")
        userpoint = userpoint + 1
        print(userpoint)
        noofchances = noofchances + 1
        print("Winner")
    elif a=="g" and b=="w":
        print(f"Your choice is  {a} and computer choice is {b}")
        computerpoint = computerpoint + 1
        noofchances = noofchances + 1
        print(computerpoint)
        print("Your are loser ")
    elif a=="g" and b=="g":
        print(f"Your choice is  {a} and computer choice is {b}")
        print("Tie ")
        noofchances = noofchances + 1
    else:
        print("Wrong Input ")
    print(" user point=",userpoint,"computer point= ",computerpoint)

print("Game over ")
if userpoint>computerpoint:
    print("winner of the match")
else :
    print("Loser")





















