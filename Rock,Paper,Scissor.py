import random

choices = ['rock', 'paper', 'scissors']

def get_computer_choice():
    return random.choice(choices)

def get_user_choice():
    input_choice = input("Enter your choice (rock/paper/scissors) or 'quit' to exit: ").lower()
    return input_choice

def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') \
         or (user_choice == 'paper' and computer_choice == 'rock') \
         or (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def update_score(winner, score):
    if winner == "You win!":
        score += 1
    elif winner == "Computer wins!":
        score -= 1
    return score

def display_score(score):
    print(f"Current Score: {score}")

def play_game():
    score = 0
    print("Welcome to Rock, Paper, Scissors!")
    print("---------------------------------")
    print("Instructions:")
    print("Type 'rock', 'paper', or 'scissors' to play.")
    print("Type 'quit' to exit the game.")
    print("---------------------------------")

    while True:
        user_choice = get_user_choice()
        if user_choice == 'quit':
            print("Thanks for playing! Final Score:", score)
            break
        elif user_choice not in choices:
            print("Invalid choice. Try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        winner = get_winner(user_choice, computer_choice)
        print(winner)

        score = update_score(winner, score)
        display_score(score)

# Run the game
play_game()
