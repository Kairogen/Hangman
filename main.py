from os import system
import random

hangmen = [
"""
  ---\\
  |  |
     |
     |
     |
     |
-----------
""",
"""
  ---\\
  |  |
  O  |
     |
     |
     |
-----------
""",
  """
  ---\\
  |  |
  O  |
  |  |
     |
     |
-----------
""",
  """
  ---\\
  |  |
  O  |
  |\ |
     |
     |
-----------
""",
  """
  ---\\
  |  |
  O  |
 /|\ |
     |
     |
-----------
""",
  """
  ---\\
  |  |
  O  |
 /|\ |
   \ |
     |
-----------
""",
  """
  ---\\
  |  |
  O  |
 /|\ |  <----- He's dead.
 / \ |
     |
-----------
""",
]

def has_numbers(inputString):
  return any(char.isdigit() for char in inputString)

def show_hangman(counter):
  print(hangmen[counter])

def get_word():
  file = open("words.txt")
  words = file.read()
  lst_ver = words.split(",")
  file.close()
  return random.choice(lst_ver)
  

correct_word = get_word()
wrong_counter = 0
list_user_view = ["_" for letter in correct_word]
wrong_guesses = []
str_user_view = " ".join(list_user_view)

while wrong_counter < 6 and "_" in str_user_view:
  show_hangman(wrong_counter)
  print(str_user_view)
  print("\nwrong guesses:")
  print(wrong_guesses)
  guess = input ("guess:")
  system("clear")
  # if they give nonsense input, don't penelize them, but warn them
  if guess in wrong_guesses or guess in list_user_view:
    print("Oops! You have already done that. No wrong guesses were added.")
  elif has_numbers(guess):
    print("Oops! You put numbers in your answer. No wrong guesses were added.")
  # else if guess is one character, check if it is in the word
  elif len(guess) == 1:
    # check if letter is in the word
    if guess in correct_word:
      indexes = [i for i, j in enumerate(correct_word) if j == guess]
      for i in indexes:
        list_user_view[i] = guess
      str_user_view = " ".join(list_user_view)
    else:
      wrong_counter += 1
      wrong_guesses.append(guess)
  # else if they give a word check if it is the correct one
  elif len(guess) > 1:
    if guess == correct_word:
      list_user_view = [letter for letter in correct_word]
      str_user_view = " ".join(list_user_view)

system("clear")
show_hangman(wrong_counter)
print(str_user_view)
if wrong_counter == 6:
  print ("You lost.")
  print ("the correct word was " + correct_word)
else:
  print("Hooray! You won.")
