# Rock,paper, scissor game
import random
option=["rock","paper","scissor"]
while True:
    print("Welcome the Rock Paper Scissor Game")
    user_point=0
    computer_point=0
    0=="rock"
    1=="paper"
    2=="scissor"
    i=1
    while i<=3:
        print("rount",i,"Start" )
        print("please select your option ")
        user_option=int(input("Enter the number of your option between 0 to 2 :"))
        computer_option=random.randint(0,2)
        print("computer option :",computer_option)
        if user_option=="end the game":
            print("The game has end")
            break
        elif user_option==computer_option:
            print("drop")    
        elif (user_option==1 and computer_option==0) or (user_option==2 and computer_option==1) or (user_option==0 and computer_option==2):
            user_point+=1
            print("You win",user_point) 
        else:
            computer_point+=1
            print("computer win",computer_point)
        i+=1
    if user_point>computer_point:
        print("you win")
        print("user point =",user_point,":","computer point =",computer_point)
        break
    elif computer_point>user_point:
        print("computer win")
        print("computer point =",computer_point,":","user point =",user_point)
        break
    else:
        print("same point bothe of you")
        print("computer point =",computer_point,":","user point =",user_point)
        user=("can you play again game - Yes or No ")
        if user=="yes" or user=="YES" or user=="Yes":
            print("Ok,Let's continue")
        else:
            break
    