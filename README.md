# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Milestone 1

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
 
