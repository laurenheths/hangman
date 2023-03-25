# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Milestone 2

This Milestone is made up of 4 tasks:
1. Create a list of 5 fruits and print in the terminal.
2. Use a function to randomly select and item from the list:
  ``` python
  random.choice()
  ```
3. Create an input function for user to enter a single letter.
4. Use an if statement to make sure the user inputs a single letter from the alphabet.
  ``` python
  guess = input("enter a single letter: ")
if len(guess) == 1 and guess.isalpha():
    print("Good Guess!")
else:
    print("Oops! That is not a valid input")
 ```
 
## Milestone 3

In this task I needed to 
```
install random-word
```
This allowed me to take a random word from a list in my code.

In this Milestone I created 2 functions.
1. A function which asked a user to input an alphabetical letter and validated that it is a single letter from the alphabet.
2. A function which checks if it is in a random word from a list.

``` python
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
```

I called the guess_check funtion inside my ask_for_input to make sure it checked if the letter was in the word after it made sure the input was valid.

## Milestone 4 

Used a class to create the hangman game.

Created 2 methods to validate the game and produce an outcome.

``` python

import random

word_list = ["apple", "banana", "pear", "orange", "strawberry", "grapes"]

class Hangman():
     def __init__(self, word_list, num_lives=5):
          self.word_list = word_list
          self.word = random.choice(word_list)
          self.word_guessed = ["_"] * len(self.word)
          self.num_letters = len(self.word)
          self.num_lives = num_lives
          self.list_of_guesses = []
          
     def check_guess(self, guess):
        guess.lower()
        if guess in self.word:
            print(f"Good Guess! {guess} is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
            self.num_letters = self.num_letters - 1
            print(self.word_guessed)
        else:
            print(f"Sorry, {guess} is not in the word. Try again")
            self.num_lives = self.num_lives - 1
            print(f"You have {self.num_lives} lives left")


     def ask_for_input(self):
        while self.num_lives > 0:
            guess = input("enter a single letter: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter, please enter a single alphabetical letter")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)
        print("Game Over!")

Hangman_1 = Hangman(word_list)
Hangman_1.ask_for_input()

```

