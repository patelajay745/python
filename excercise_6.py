import random

mylist = ["snake", "water", "gun"]

user_win=computer_win=draw=0

i=1

while (i<=5):
    user_choice=input("What you want to choose? s for snake, w for water and g for gun : ")
    Computer_choice=random.choice(mylist)
    if (user_choice=="s"):
        if(Computer_choice=="water"):
            user_win+=1
            print("You won")
        elif(Computer_choice=="gun"):
            computer_win+=1
            print("You lost")
        else:
            draw+=1
            print("draw")
    elif (user_choice=="w"):
        if(Computer_choice=="snake"):
            computer_win+=1
            print("You lost")
        elif(Computer_choice=="gun"):
            user_win+=1
            print("You won")
        else:
            draw+=1
            print("draw")
    elif (user_choice=="g"):
        if(Computer_choice=="snake"):
            user_win+=1
            print("You won")
        elif(Computer_choice=="water"):
            computer_win+=1
            print("You lost")
        else:
            draw+=1
            print("draw")
    else:
        print("wrong input")        
    i+=1
if(computer_win > user_win):
    print(f"You lost game by {computer_win}-{user_win}")
elif(user_win>computer_win):
    print(f"You won game by {user_win}-{computer_win}")
else:
    print(f"game is draw by {user_win}-{computer_win} ")