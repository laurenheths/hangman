import random

word_list = ["apple", "banana", "pear", "orange", "strawberry", "grapes"]

class Hangman():
     def __init__(self, word_list, num_lives=5):
          self.word_list = word_list
          self.word = random.choice(word_list)
          self.word_guessed = ["_"] * len(self.word)
          self.num_letters = len(set(self.word))
          self.num_lives = num_lives
          self.list_of_guesses = []
          
     def check_guess(self, guess):
        guess = guess.lower()
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
            guess = input("enter a single letter: ")
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
        if game.num_lives < 1:
            print("You Lost!")
            break
        elif game.num_letters < 1:
            print("Congratulations, you won the game!")
            break
        else:
            print(game.num_letters)
            game.ask_for_input()

play_game(word_list)           
