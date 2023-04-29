import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Hello World Game")

# Set up the font
font = pygame.font.Font(None, 36)

# Create a text surface
text = font.render("Hello World", True, (255, 255, 255))

# Main game loop
running = True
while running:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the text
    screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()