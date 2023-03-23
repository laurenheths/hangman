from random_word import RandomWords

r = RandomWords()
word = r.get_random_word()
print(word)

while True:
    guess = input("enter a single letter: ")
    if len(guess) == 1 and guess.isalpha() and guess in word:
         print(f"Good Guess! {guess} is in the word.")
    else:
         print(f"Sorry, {guess} is not in the word. Try again")
