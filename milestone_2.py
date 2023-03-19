import random

word_list = ['strawberries', 'raspberries', 'apples', 'bananas', 'grapes']
print(word_list)

word = random.choice(word_list)
print(word)

guess = input("enter a single letter: ")
