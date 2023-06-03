import pygame
import sys
import constants
import sandbox

# Initialize Pygame
pygame.init()

# Set up the display
clock = pygame.time.Clock()
screen = pygame.display.set_mode((constants.screen_width, constants.screen_height))
pygame.display.set_caption("Internity Grove")
dev_sandbox = sandbox.Sandbox()

# Main game loop
running = True
while running:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw Sandbox
    dev_sandbox.draw(screen)

    # Update the display
    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()