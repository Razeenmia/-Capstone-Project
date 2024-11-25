import random

def get_user_choice():
    """Get the user's choice of Rock, Paper, or Scissors."""
    while True:
        user_choice = input("Enter Rock, Paper, or Scissors: ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please enter 'Rock', 'Paper', or 'Scissors'.")

def get_computer_choice():
    """Randomly select Rock, Paper, or Scissors for the computer."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the user's and computer's choices."""
    if user_choice == computer_choice:
        return "It's a tie!"
    
    # Winning conditions
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'paper' and computer_choice == 'rock') or \
       (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    
    return "You lose!"

def play_game():
    """Play the Rock, Paper, Scissors game."""
    print("Welcome to Rock, Paper, Scissors!")
    
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"\nYou chose: {user_choice}")
    print(f"The computer chose: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)

# Run the game
if __name__ == "__main__":
    play_game()
