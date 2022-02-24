import random
from art import logo

def instructions():
    print(logo)
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    level = ''
    while level != 'easy' and level != 'hard':
        level = input("Choose a difficulty. Type 'easy' or 'hard:' ").casefold()
    return level


def get_random_integer():
    return random.randint(1,100)

level = instructions()
answer = get_random_integer()
lives = 5 if level == 'hard' else 10

while True:
    plural = 's' if lives > 1 else ''
    print(f"You have {lives} attempt{plural} remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == answer:
        break
    elif guess < answer:
        print("Too low.")
    elif guess > answer:
        print("Too high.")
    
    lives -= 1
    if lives >= 1:
        print("Guess again.")
    if lives == 0:
        break

if guess == answer:
    print("Well done! You guessed the number.")
else:
    print(f"Unlucky. The number was {answer}.")

