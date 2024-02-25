ageOrBirth=input("Enter age or year of birth: ")

try:
    ageOrBirth=int(ageOrBirth)
    if(ageOrBirth<100):
        currentAge=ageOrBirth
        print(f" you will be turn 100 years old by {2024+(100-age)} ")
    
    elif(ageOrBirth>1924 and ageOrBirth<=2024):
        currentAge=2024-ageOrBirth
        print(f" you current age is {currentAge} ")
        print(f" you will be turn 100 years old by {2024+(100-currentAge)} ")
    elif(ageOrBirth>100 or ageOrBirth<1924):
        print("You seeems to be the oldest person alive")
        exit()
    userInput=(input("Do You want to check you age in perticular year? Type Yes or no : ")).lower()

    if(userInput=="yes"):
        enteredYear=int(input("Enter the year in which you want to check your age: "))
        print(f"You age will be {(enteredYear-2024)+currentAge} in {enteredYear} year. ")
    elif(userInput=="no"):
        pass
    else:
        print("Please enter valid input")

except ValueError:
    # Handle the exception
    print('Please enter valid input')
except Exception as e:
    print(str(e)) 
