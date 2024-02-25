n=18


attempt=1

while(attempt<=9):
    if(int(input("Guess the number: "))==18):
        print("Right, you took"+ str(attempt) +" guesses to finish it")
        break
    else:
        print("No of guesses left : "+ str(9-attempt))
        attempt=attempt+1
