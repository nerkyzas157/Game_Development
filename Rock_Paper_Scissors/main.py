# Rock, Paper, Scissors game simulator
import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
ready = "y"
pc = random.randint(1, 3)
p_rock = 1
p_paper = 2
p_scissors = 3

while ready == "y":
    player = input("What's your choice? \n(rock/paper/scissors) ")
    player = player.lower()
    if player == "rock" and pc == 1:
        print(f"Player chose:\n{rock}\n Computer chose:\n{rock}\nIt's a draw!")
    elif player == "rock" and pc == 2:
        print(f"Player chose:\n{rock}\n Computer chose:\n{paper}\nYou lost!")
    elif player == "rock" and pc == 3:
        print(f"Player chose:\n{rock}\n Computer chose:\n{scissors}\nYou won!")
    elif player == "paper" and pc == 1:
        print(f"Player chose:\n{paper}\n Computer chose:\n{rock}\nYou won!")
    elif player == "paper" and pc == 2:
        print(f"Player chose:\n{paper}\n Computer chose:\n{paper}\nIt's a draw!")
    elif player == "paper" and pc == 3:
        print(f"Player chose:\n{paper}\n Computer chose:\n{scissors}\nYou lost!")
    elif player == "scissors" and pc == 1:
        print(f"Player chose:\n{scissors}\n Computer chose:\n{rock}\nYou lost!")
    elif player == "scissors" and pc == 2:
        print(f"Player chose:\n{scissors}\n Computer chose:\n{paper}\nYou won!")
    elif player == "scissors" and pc == 3:
        print(f"Player chose:\n{scissors}\n Computer chose:\n{scissors}\nIt's a draw!")
    else:
        print("Invalid choice.")
    ready = input("Are you ready to play again? \n(y/n)")
    ready = ready.lower()
