import pygame
import constants

class Sandbox:
    def __init__(self):
        self.surface = pygame.Surface((1440, 810))
        self.surface.fill((255, 255, 255))

    def draw(self, screen):
        screen.blit(self.surface, (constants.screen_width // 2 - self.surface.get_width() // 2, constants.screen_height // 2 - self.surface.get_height() // 2))