from random import randint
from proj_art import logo


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(user_guess, answer, turns):
    if user_guess > answer:
        print("Too high.")
        return turns - 1
    elif user_guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"Correct! The answer is {answer}.")


def difficulty():
    difficulty_input = input("Choose the difficulty: (easy/hard) ").lower()
    if difficulty_input == "hard":
        return HARD_LEVEL_TURNS
    elif difficulty_input == "easy":
        return EASY_LEVEL_TURNS


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    # print(f"Pssst, the correct answer is {answer}")
    turns = difficulty()
    print(f"You have {turns} attempts to guess the number.")
    guess = 0
    while guess != answer:
        guess = int(input("Input your guess between 1 and a 100: "))
        turns = check_answer(guess, answer, turns)
        print(f"You have {turns} attempts remaining to guess the number.")
        if turns == 0:
            print("You ran out of lives.")
            return
        elif guess != answer:
            print("Guess again.")


game()
