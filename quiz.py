import os
# Clears the screen
def clear_screen(message=''):
    os.system('cls' if os.name == 'nt' else 'clear')
    if message != '':
        print(message)
#Welcome message and point variable
print('Welcome to the Halo Quiz!')
answers_correct = 0
points = answers_correct
#Main menu of the quiz
def main_menu():
  playing = input('Do you want to begin? (y/n) ').lower()
  while True:
    if playing == 'y':
      print('Lets begin!')
      question_one()
      break
    elif playing == 'n':
      print('Your loss!')
      break
    else:
      print('Invalid input, please type "y" or "n" ')
      main_menu()
#Questions are listed below
def question_one():
  clear_screen()
  global points
  print('''What year did Halo: Combat Evolved release? \n
  a) 2003
  b) 2001
  c) 2000
  d) 1999''')
  answer = input('').lower()
  while True:
    if answer != 'b':
      print('Incorrect! Halo: CE was released in 2001 \n')
      input('Press Enter to continue...')
      question_two()
      break
    else:
      points += 1
      print(f'Correct! You earned 1 point! Your total points is now: {points} \n')
      print('')
      input('Press Enter to continue...')
      question_two()
      break      
def question_two():
  clear_screen()
  global points
  print("""Who voices the Master Chief? \n
  a) Steve Downes
  b) Chris Farley
  c) Keith David
  d) Seth McFarlan
  """)
  answer = input('').lower()
  while True:
    if answer !='a':
      print('Incorrect! Steve Downes voices the Master Chief \n')
      input('Press Enter to continue...')
      question_three()
      break
    else:
      points += 1
      print(f'Correct! You earned 1 point! Your total points is now: {points} \n')
      input('Press Enter to continue...')
      question_three()
      break      
def question_three():
  clear_screen()
  global points
  print("""What rank is Sergeant Johnson? \n
  a) Sergeant
  b) Command Sergeant Major
  c) Platoon Sergeant
  d) Sergeant Major
  """)
  answer = input('').lower()
  while True:
    if answer !='d':
      print('Incorrect! Sergeant Johnson is a Sergeant Major. \n')
      input('Press Enter to continue...')
      total_points()
      break
    else:
      points += 1
      print(f'Correct! You earned 1 point! Your total points is now: {points} \n')
      input('Press Enter to continue...')
      total_points()
      break
#Takes the total points and returns a % correct
def total_points():
  global points
  clear_screen()
  total_points = (points / 3) * 100
  print(f'For this attempt you earned a {total_points:.1f}%. \n')
  input('Would you like to retake the quiz? (y/n) ').lower()
  #Retaking the quiz 0's out your points and returns to the main menu
  while True:
    if input != 'y':
      points = 0
      main_menu()
      break
    else:  
      print('You may now exit the program')
      input('Press Enter to Exit...')
main_menu()


