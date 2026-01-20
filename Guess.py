import random

def get_user_guess():
    return int(input("Enter your guess (1-10): "))

def secret_number_game():
    print("Welcome to the Secret Number Guessing Game!")
    secret_number = random.randint(1, 10)
    attempts = 0

    while True:
        guess = get_user_guess()
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed {secret_number} in {attempts} attempts.")
            break

# Run the game
secret_number_game()

