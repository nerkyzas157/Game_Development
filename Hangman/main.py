import hangman_art
import random
import hangman_words

print(
    f"{hangman_art.logo}\n\nWelcome to the Hangman game!\nA random word will be chosen for this game.\nIf you make 6 mistakes, you loose.\nGood luck!"
)

gameover = False
chosen_word = random.choice(hangman_words.word_list)
lives = 6
incorrect = []

# For each letter in the chosen_word, add a "_" to 'display'.
display = []
lett = len(chosen_word)
for i in range(lett):
    display.append("_")

print(f"\nWord to guess: {' '.join(display)}\n")

print(hangman_art.stages[lives])

while gameover == False:
    # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("\nGuess the letter in a word:\n").lower()
    # Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    # If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    position = -1
    count = 0
    for i in chosen_word:
        if i == guess:
            position += 1
            display[position] = guess
            count += 1
        else:
            position += 1
    print(f"Your guessed letter appeared {count} time/s in the hidden word")
    if count == 0:
        incorrect.append(guess)
        lives -= 1
        print(
            f"Your guessed letter ({guess}) is not in the word. You have {lives} lives left.\n{hangman_art.stages[lives]}"
        )
    if lives > 0:
        print(f"\nWord to guess: {' '.join(display)}\n")
    if len(incorrect) > 0:
        print(f"\nIncorrectly guessed letters: {', '.join(incorrect)}\n")
    if "_" not in display:
        gameover = True
        print("\nYou won!\n")
    if lives == 0:
        print(f"\nYou lost! The word was '{chosen_word}'.\n")
        gameover = True
