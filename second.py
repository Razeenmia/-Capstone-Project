import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Rock, Paper, Scissors Game')

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Define fonts
font = pygame.font.Font(None, 36)

# Define possible moves
moves = ['rock', 'paper', 'scissors']

# Function to display text
def display_text(text, x, y, color):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))

# Function to determine winner
def get_winner(player_move, computer_move):
    if player_move == computer_move:
        return 'Draw'
    elif (player_move == 'rock' and computer_move == 'scissors') or \
         (player_move == 'paper' and computer_move == 'rock') or \
         (player_move == 'scissors' and computer_move == 'paper'):
        return 'You Win!'
    else:
        return 'You Lose!'

# Main game loop
def game_loop():
    user_choice = None
    computer_choice = None
    result = ''
    
    # Buttons for user choice
    rock_button = pygame.Rect(100, 300, 100, 50)
    paper_button = pygame.Rect(250, 300, 100, 50)
    scissors_button = pygame.Rect(400, 300, 100, 50)
    
    while True:
        screen.fill(WHITE)
        
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # Check if the user clicked any of the buttons
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if rock_button.collidepoint(mouse_pos):
                    user_choice = 'rock'
                elif paper_button.collidepoint(mouse_pos):
                    user_choice = 'paper'
                elif scissors_button.collidepoint(mouse_pos):
                    user_choice = 'scissors'
                
                # If user makes a choice, let the computer make a random choice
                if user_choice:
                    computer_choice = random.choice(moves)
                    result = get_winner(user_choice, computer_choice)
        
        # Draw buttons
        pygame.draw.rect(screen, GREEN, rock_button)
        pygame.draw.rect(screen, GREEN, paper_button)
        pygame.draw.rect(screen, GREEN, scissors_button)
        
        # Display button texts
        display_text('Rock', 120, 315, BLACK)
        display_text('Paper', 270, 315, BLACK)
        display_text('Scissors', 410, 315, BLACK)
        
        # Display the choices and result
        if user_choice:
            display_text(f'Your choice: {user_choice}', 200, 100, BLACK)
            display_text(f'Computer\'s choice: {computer_choice}', 200, 150, BLACK)
            display_text(f'Result: {result}', 200, 200, RED)
        
        # Update the screen
        pygame.display.update()

# Run the game
game_loop()
import pygame
pygame.mixer.quit()  # Disable audio mixer
pygame.init()
