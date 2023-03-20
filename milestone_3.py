while True:
    guess = input("enter a single letter: ")
    if len(guess) == 1 and guess.isalpha():
         break
    else:
         print("Invalid lesster, please enter a single alphabetical character")
