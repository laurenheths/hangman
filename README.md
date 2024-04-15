# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Aim
The code selects a word at random from a given list using the Hangman class. Upon initialisation, this class sets up several attributes, including the word list, the selected word itself, a representation of the word with underscores for unrevealed letters, the count of unique letters in the chosen word, the number of lives available, and a list to store guessed letters. When a player inputs a letter, the code checks if it exists in the chosen word. 
If correct, it updates the representation of the word, decrements the count of remaining unique letters to guess, and provides feedback on the number of remaining letters. Input validation ensures that only single alphabetical letters are accepted. The game continues in a loop until either the player runs out of lives, resulting in a "You Lost!" message, or successfully guesses all letters, triggering a "Congratulations, you won the game!" message. The main function initializes the word list and initiates the game.

## Features
1. Random Word Selection: The Hangman class randomly selects a word from the provided word list using the random.choice() function.

2. Initialization: The Hangman class has an __init__ method that initializes various attributes such as word_list, word, word_guessed, num_letters, num_lives, and list_of_guesses.

3. Word Guessing Mechanism: The check_guess method checks if the guessed letter is present in the chosen word. It updates the word_guessed attribute accordingly and decrements the num_letters attribute if the guess is correct.

4. Input Validation: The ask_for_input method validates the user input, ensuring that it is a single alphabetical letter.

5. Game Loop: The play_game function runs a loop until the game is won or lost, based on the conditions of num_lives and num_letters.

6. Win/Loss Conditions: The game ends with a "You Lost!" message if the player runs out of lives (num_lives == 0). It ends with a "Congratulations, you won the game!" message if all letters in the word are guessed (num_letters == 0).

7. Main Function: The main function initialises the word list and starts the game by calling the play_game function.

## Installation
To install the Hangman game, follow these steps:

1. **Clone the Repository** : Begin by cloning the repository containing the Hangman game code. You can do this by running the following command in your terminal:
'''
git clone <repository_url>
'''
Replace <repository_url> with the URL of the repository.

2. **Navigate to the Directory** : Move into the directory where the code is located. Use the cd command in your terminal:
'''
cd hangman-game
'''
3. **Run the Game** : Once you're in the correct directory, you can run the game by executing the Python script. Use the following command:
'''
python hangman.py
'''
4. **Enjoy the Game** : The Hangman game should now start running in your terminal. Follow the on-screen instructions to play the game.

### Prerequisites

- Python: Download and install Python from the [official website](https://www.python.org/downloads/).
- Git (Optional): If you plan to clone the repository, you'll need Git installed on your system. Download Git from the [official website](https://git-scm.com/downloads).

### The Final Code

``` python
import random


class Hangman():
     def __init__(self, word_list, num_lives=5):
          self.word_list = word_list
          self.word = random.choice(word_list)
          self.word_guessed = ["_"] * len(self.word)
          self.num_letters = len(set(self.word))
          self.num_lives = num_lives
          self.list_of_guesses = []
          
     def check_guess(self, guess):
        if guess in self.word:
            print(f"Good Guess! {guess} is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
            self.num_letters = self.num_letters - 1
            print(self.word_guessed)
            print(f"you have {self.num_letters} letters left to guess!")
        else:
            print(f"Sorry, {guess} is not in the word. Try again")
            self.num_lives = self.num_lives - 1
            print(f"You have {self.num_lives} left!")


     def ask_for_input(self):
            guess = input("enter a single letter: ").lower()
            
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter, please enter a single alphabetical letter")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print("You Lost!")
            break
        elif game.num_letters == 0:
            print("Congratulations, you won the game!")
            break
        else:
            game.ask_for_input()

if __name__ == "__main__":
    word_list = ["apple", "banana", "pear", "orange", "strawberry", "grapes"]
    play_game(word_list)

```

