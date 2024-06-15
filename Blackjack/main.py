############### Blackjack Project #####################
from art import logo
import random

player = []
dealer = []
player_score = 0
dealer_score = 0
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def player_ace(player):
    if 11 in player and sum(player) > 21:
        player.remove(11)
        player.append(1)
    return player


def dealer_ace(dealer):
    if 11 in dealer and sum(dealer) > 21:
        dealer.remove(11)
        dealer.append(1)
    return dealer


def blackjack(player, dealer, player_score, dealer_score):
    """Fuction provides the full game by dealing cards, checking for Blacjacks, allowing user input for hit/pass moves and announcing the winner."""
    player = random.choices(cards, k=2)
    dealer = random.choices(cards, k=2)
    player_ace(player)
    dealer_ace(dealer)
    player_score = sum(player)
    dealer_score = sum(dealer)
    print(f"Your cards: {player}, current score: {player_score}")
    print(f"Dealer's first card: {dealer[0]}")
    if player_score == 21 and dealer_score == 21:
        return print(
            f"\nYour final hand: {player}, final score: {player_score}\nDealer's final hand: {dealer}, final score: {dealer_score}\nIt's a draw.\n"
        )
    elif player_score == 21:
        return print(
            f"\nYour final hand: {player}, final score: {player_score}\nDealer's final hand: {dealer}, final score: {dealer_score}\nBlackjack! You won!\n"
        )
    elif dealer_score == 21:
        return print(
            f"\nYour final hand: {player}, final score: {player_score}\nDealer's final hand: {dealer}, final score: {dealer_score}\nDealer won with a Blackjack.\n"
        )
    choice = True
    while choice == True:
        choice_input = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if choice_input == "y":
            choice = True
            player.append(random.choice(cards))
            player_ace(player)
            player_score = sum(player)
            print(f"Your cards: {player}, current score: {player_score}")
            if player_score > 21:
                return print(
                    f"\nYour final hand: {player}, final score: {player_score}\nDealer's final hand: {dealer}, final score: {dealer_score}\nYou busted. Dealer won.\n"
                )
        else:
            choice = False
    while dealer_score < 17:
        dealer.append(random.choice(cards))
        dealer_ace(dealer)
        dealer_score = sum(dealer)
        if dealer_score > 21:
            return print(
                f"\nYour final hand: {player}, final score: {player_score}\nDealer's final hand: {dealer}, final score: {dealer_score}\nDealer busted. You win!\n"
            )
    if dealer_score > player_score:
        return print(
            f"\nYour final hand: {player}, final score: {player_score}\nDealer's final hand: {dealer}, final score: {dealer_score}\nYou lost.\n"
        )
    elif dealer_score == player_score:
        return print(
            f"\nYour final hand: {player}, final score: {player_score}\nDealer's final hand: {dealer}, final score: {dealer_score}\nIt's a draw.\n"
        )
    else:
        return print(
            f"\nYour final hand: {player}, final score: {player_score}\nDealer's final hand: {dealer}, final score: {dealer_score}\nYou win!\n"
        )


print("Helllo and welcome to my Blackjack game!")
play = True
while play == True:
    play_input = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': "
    ).lower()
    if play_input == "y":
        play = True
        print(logo)
        blackjack(player, dealer, player_score, dealer_score)
    else:
        play = False
