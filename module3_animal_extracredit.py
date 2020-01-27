import random

animal_list = ["dog", "cat", "bird", "cow", "pig", "horse", "snake", "lizard"]
guess = random.choice(animal_list)
newlist = len(guess)*"-"
newlist = list(newlist.lower())
namelength = int(len(guess))
maxguess = int(3+namelength)
remaining = maxguess


#guess = list(guess.lower())
#count = 0


print("\n"
      "Welcome to the guess one of my favorite animals game!  Enter letters one at a time.\n"
      "You have",maxguess,"guesses. What is your first letter?")

while True:

    if newlist == list(guess):
        print("You guessed it!")
        break
    if remaining == -1:
        print("Sorry no more tries, someone still loves you!")
        break
    user_guess = input("\n What's your guess?: ")
    user_guess = user_guess.lower()
    if user_guess.isnumeric():
        print("Only letters, not numbers!")
    elif len(str(user_guess)) > 1:
        print("Single letters only!")
    else:
        remaining -= 1
        for letter in guess:
            if letter == user_guess:
                guess.index(letter)
                newlist[guess.index(letter)] = letter
                print("Partial Match. You have", remaining, 'guesses left.')
                print(' '.join(newlist))
        if user_guess not in guess:
            print("No Match. You have",remaining, 'guesses left.')







