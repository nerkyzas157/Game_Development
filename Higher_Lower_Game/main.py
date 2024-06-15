# Importing the requirments
import art
from game_data import data
from random import randint

# Creating the global variables
score = 0
play_loop = True


# Funtion to clear the screen
def clear():
    i = "\n" * 100
    print(i)


# Game output
def game(score, a_temp, b_temp):
    # Defining local variables
    a_name = data[a_temp]["name"]
    a_description = data[a_temp]["description"]
    a_country = data[a_temp]["country"]
    b_name = data[b_temp]["name"]
    b_description = data[b_temp]["description"]
    b_country = data[b_temp]["country"]
    # Creating interaction
    clear()
    print(art.logo)
    if score > 0:
        print(f"You're right! Current score: {score}.\n")
    print(f"Compare A: {a_name}, a {a_description}, from {a_country}.")
    print(art.vs)
    print(f"\nCompare B: {b_name}, a {b_description}, from {b_country}.\n")


# Checking if guess was correct by comparing the follower count between A and B
def compare(a_temp, b_temp):
    # Importing global variable, so it could be manipulated
    global score
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    # Defining local comparables
    a_follower_count = data[a_temp]["follower_count"]
    b_follower_count = data[b_temp]["follower_count"]
    if answer == "a":
        if a_follower_count > b_follower_count:
            score += 1
        else:
            print(f"\nSorry, that's wrong. Final score: {score}.")
            score = 0
    else:
        if a_follower_count < b_follower_count:
            score += 1
        else:
            print(f"\nSorry, that's wrong. Final score: {score}.")
            score = 0


while play_loop == True:
    # Generating random integers and saving the values
    a_random = randint(0, len(data) - 1)
    b_random = randint(0, len(data) - 1)
    a_temp = a_random
    b_temp = b_random
    game(score, a_temp, b_temp)
    compare(a_temp, b_temp)
    # Asking player if they would like to try again
    if score == 0:
        again = input("Would you like to play again? (Y/N) ").lower()
        if again == "y":
            play_loop == True
        else:
            break
