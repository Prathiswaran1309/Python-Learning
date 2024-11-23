import random

def number_guessing_game():
    number_to_guess = random.randint(1,51)
    attempts = 0
    max_attempts = 3
    guess = None

    print("Welcome to the Number Guessing Game!")

    while guess != number_to_guess and attempts<max_attempts:
        guess = int(input("Guess the number(between 1 and 50):"))
        attempts +=1

        if guess<number_to_guess:
            print("Too low!")
        elif guess>number_to_guess:
            print("Too high!")

    if guess == number_to_guess:
        print(f"Correct! You guessed it in {attempts} tries.")
    else:
        print(f"Sorry!You've used all {max_attempts} attempts. The correct number was {number_to_guess}.")

number_guessing_game()