import random
throw = random.randint(1, 3)
hand = ""
print("Welcome to Rock, Paper, Scissors! \n")
def start():
  while True:
    global user_turn
    user_turn = input("rock, paper, or scissors? \n").lower()
    if user_turn == "rock":
      cpu_turn()
      break
    elif user_turn == "paper":
      cpu_turn()
      break
    elif user_turn == "scissors":
      cpu_turn()
      break
    else:
      print("You didn't select a valid option!")
      continue
  return user_turn

def cpu_turn():
  while True:
    if throw == 1:
      hand = "rock"
      print(f"You threw {user_turn} and the computer threw {hand}!")
      who_won()
      break
    elif throw == 2:
      hand = "paper \n"
      print(f"You threw {user_turn} and the computer threw {hand}!")
      who_won()
      break
    else:
      hand = "scissors \n"
      print(f"You threw {user_turn} and the computer threw {hand}!")
      who_won()
      break

def who_won():
  if throw == 1 and user_turn == "paper":
    print("You won!")
  elif throw == 2 and user_turn == "scissors":
    print("You won!")
  elif throw == 3 and user_turn == "rock":
    print("You won!") 
  elif throw == 1 and user_turn == "rock":
    print("It is a tie!")
  elif throw == 2 and user_turn == "paper":
    print("It is a tie!")
  elif throw == 3 and user_turn == "scissors":
    print("It is a tie!")
  elif throw == 1 and user_turn == "scissors":
    print("You lost!")
  elif throw == 2 and user_turn == "rock":
    print("You lost!")
  else:
    print("You lost!")
start()

