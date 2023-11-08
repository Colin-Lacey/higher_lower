from game_data import data
from art import logo, vs
import random
import os

print(logo)
playing = True
score = 0
b = random.choice(data)

# Main game loop
while playing:
  # Initially 'a' is set to the random 'b' from game start, and every other iteration, 'a' is the last 'b'
  a = b
  # 'b' is a new random entry from game_data for every every iteration of the game
  b = random.choice(data)
  # Loop to make sure b!=a; finishes when 'a' and 'b' are different
  while a == b:
    b = random.choice(data)

  # Get the account ('a' or 'b') with the most instagram followers
  higher = 'a' if a['follower_count'] > b['follower_count'] else 'b'

  # Main game display
  print(f"Compare A: {a['name']}, a {a['description']} from {a['country']}")
  print(vs)
  print(f"Against B: {b['name']}, a {b['description']} from {b['country']}")
  # Get user's guess of highest followers: 'a' or 'b'
  user_highest_guess = input(
    "\nWho has more Instagram followers? Type 'a' or 'b': ").lower()

  # Simple input checking
  while user_highest_guess != 'b' and user_highest_guess != 'a':
    user_highest_guess = input("That is not a valid response. Please type 'a' or 'b': ").lower()
  # Clear the game displya before displaying result
  os.system('clear')

  # If user guessed right
  if user_highest_guess == higher:
    score += 1
    print(logo)
    print(f"\nCorrect! Your score is {str(score)}.\n")
  # If user guessed wrong - notify and ask if they want to restart the game
  else:
    print(f"Incorrect! You finished with a score of {str(score)}")
    response = input(
      "Do you want to keep playing? Type 'y' to continue or anything else to quit: "
    )
    os.system('clear')
    if response.lower() != 'y':
      playing = False
    else:
      print(logo)
      score = 0
      b = random.choice(data)
