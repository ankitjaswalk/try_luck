import random

def guess_the_number():
    number_to_guess = random.randint(1, 10)
    attempts = 3

    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 10.")
    print(f"You have {attempts} attempts to guess it.\n")

    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}: Enter your guess: "))
            if guess < 1 or guess > 10:
                print("Please enter a number between 1 and 10.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if guess == number_to_guess:
            print(f"Congratulations! You guessed it right in {attempt} attempt(s).")
            break
        elif guess < number_to_guess:
            print("Too low!")
        else:
            print("Too high!")

        if attempt == attempts:
            print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")

if __name__ == "__main__":
    guess_the_number()
