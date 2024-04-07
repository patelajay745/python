import random

def get_guess(a, b):
    return int(input(f"Please guess the number between {a} and {b}: "))

def play_turn(player, a, b):
    random_num = random.randint(a, b)
    trials = 1

    while True:
        guessed_number = get_guess(a, b)
        if guessed_number == random_num:
            print(f"{player} guessed right. It took {trials} guesses.")
            break
        elif guessed_number < random_num:
            trials += 1
            print("You guessed a smaller number. Please try again.")
        else:
            trials += 1
            print("You guessed a larger number. Please try again.")
    return trials

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

player1_trials = play_turn("Player One", a, b)
player2_trials = play_turn("Player Two", a, b)

if player1_trials == player2_trials:
    print("Both players have the same number of guesses, so no one won.")
elif player1_trials < player2_trials:
    print("Player One won.")
else:
    print("Player Two won.")
