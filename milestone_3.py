import random

word_list = ["apple", "banana", "pear"]
word = random.choice(word_list)

def check_guess(guess):
     guess.lower()
     if guess in word:
          print(f"Good Guess! {guess} is in the word.")
     else:
          print(f"Sorry, {guess} is not in the word. Try again")

def ask_for_input():
     while True:
          guess = input("enter a single letter: ")
          if len(guess) == 1 and guess.isalpha():
               break
          else:
               print("Invalid letter, please enter a single alphabetical letter")
     check_guess(guess)

ask_for_input()

