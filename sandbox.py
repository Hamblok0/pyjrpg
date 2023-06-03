import pygame
import constants
from pytmx.util_pygame import load_pygame

class Sandbox:
    def __init__(self):
        self.tmx = load_pygame('./maps/devsandbox.tmx')

    def draw(self, screen):
        for layer in self.tmx.visible_layers:
            for x, y, gid in layer:
                tile = self.tmx.get_tile_image_by_gid(gid)
                if tile:
                    screen.blit(tile, (x * self.tmx.tilewidth, y * self.tmx.tileheight))