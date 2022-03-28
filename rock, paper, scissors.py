#Easy Rock, Paper, Scissors game in Python

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

decisions = [rock, paper, scissors]


if player_choice == 0:
  print(decisions[0])
  print("Computer chose:")
  computer = random.randint(0, len(decisions) - 1)
  print(decisions[computer])
  if player_choice == 0 and computer == 0:
    print("Draw!")
  elif player_choice == 0 and computer == 1:
    print("You Loose!")
  else:
    print("You Win!")
elif player_choice == 1:
  print(decisions[1])
  print("Computer chose:")
  computer = random.randint(0, len(decisions) - 1)
  print(decisions[computer])
  if player_choice == 1 and computer == 0:
    print("You Win!")
  elif player_choice == 1 and computer == 1:
    print("Draw!")
  else:
    print("You Lose!")
elif player_choice == 2:
  print(decisions[2])
  print("Computer chose:")
  computer = random.randint(0, len(decisions) - 1)
  print(decisions[computer])
  if player_choice == 2 and computer == 0:
    print("You Lose!")
  elif player_choice == 2 and computer == 1:
    print("You Win!")
  else:
    print("Draw!")
else:
  print("Wrong number!")