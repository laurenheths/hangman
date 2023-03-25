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


