import pygame
import random
import sys

# Disable Pygame's audio system if not using sound
pygame.mixer.quit()  # This line disables the sound

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
FPS = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Fonts
font = pygame.font.SysFont("Arial", 30)
big_font = pygame.font.SysFont("Arial", 50)

# Game Choices
choices = ['rock', 'paper', 'scissors']

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock, Paper, Scissors")

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"  # If both choices are the same, it's a tie
    # Winning conditions:
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'paper' and computer_choice == 'rock') or \
       (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"  # User wins if they beat the computer's choice

    return "You lose!"  # If the user doesn't win, they lose


        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    return "You lose!"

# Function to draw the buttons
def draw_buttons():
    pygame.draw.rect(screen, BLUE, (50, 300, 150, 50))
    pygame.draw.rect(screen, GREEN, (225, 300, 150, 50))
    pygame.draw.rect(screen, RED, (400, 300, 150, 50))

    rock_text = font.render("Rock", True, WHITE)
    paper_text = font.render("Paper", True, WHITE)
    scissors_text = font.render("Scissors", True, WHITE)

    screen.blit(rock_text, (100, 315))
    screen.blit(paper_text, (255, 315))
    screen.blit(scissors_text, (430, 315))

# Function to display the result
def display_result(user_choice, computer_choice, result):
    result_text = big_font.render(result, True, BLACK)
    user_text = font.render(f"You chose: {user_choice.capitalize()}", True, BLACK)
    computer_text = font.render(f"Computer chose: {computer_choice.capitalize()}", True, BLACK)

    screen.blit(user_text, (50, 100))
    screen.blit(computer_text, (50, 150))
    screen.blit(result_text, (150, 200))

def play_game():
    user_choice = None
    computer_choice = None
    result = ""

    # Game loop
    while True:
        screen.fill(WHITE)
        draw_buttons()

        if user_choice and computer_choice:
            result = determine_winner(user_choice, computer_choice)
            display_result(user_choice, computer_choice, result)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                # User selects Rock, Paper, or Scissors based on mouse click
                if 50 <= x <= 200 and 300 <= y <= 350:
                    user_choice = 'rock'
                    computer_choice = get_computer_choice()
                elif 225 <= x <= 375 and 300 <= y <= 350:
                    user_choice = 'paper'
                    computer_choice = get_computer_choice()
                elif 400 <= x <= 550 and 300 <= y <= 350:
                    user_choice = 'scissors'
                    computer_choice = get_computer_choice()

        # Update the display
        pygame.display.update()
        pygame.time.Clock().tick(FPS)

# Run the game
if __name__ == "__main__":
    play_game()

