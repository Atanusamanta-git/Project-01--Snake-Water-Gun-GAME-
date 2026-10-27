import random
# I Make a Simple Game This game Name is "Snake, Water, Gun"
'''
1=Snake
0=Water
-1=Gun
'''
Computer =random.choice([1, 0, -1])
Youdict={"s":1, "w":0, "g":-1}
Youstr=input("Enter Your Choice in(s/w/g): ")
reversdict={1:"snake", 0:"water", -1:"gun"}
#By now we have 2 Number(Veriable)Computer And You

you=Youdict[Youstr]
print(f"You Choice {reversdict[you]} Computer Choice {reversdict[Computer]}")

if (Computer==you):
    print("This is Draw")
else:
    if(Computer==-1 and you==1):
        print("You Lose!")
    elif(Computer==-1 and you==0):
        print("You Win")
    elif(Computer==1 and you==-1):
        print("You Win")
    elif(Computer==1 and you==0):
        print("You Lose!")
    elif(Computer==0 and you==-1):
        print("You Lose!")
    elif(Computer==0 and you==1):
        print("You Win")
    else:
        print("Somthing Went Wrong!!")