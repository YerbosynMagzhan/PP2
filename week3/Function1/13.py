import random

name = input("Hello! What is your name? ")
secret_num = random.randint(1, 20)
guesses = 0

print(f"Well, {name}, I am thinking of a number between 1 and 20.")

while True:
    my_guess = int(input("Take a guess\n"))
    guesses += 1
    if my_guess == secret_num:
        print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
        break
    elif my_guess < secret_num:
        print('Your guess is too low')
    elif my_guess > secret_num:
        print('Your guess is too high')
