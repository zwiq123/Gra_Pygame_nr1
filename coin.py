import pygame
from pygame.locals import *


class Coin:
    def __init__(self, x, y, game):
        self.x = x
        self.y = y
        self.Rect = Rect(self.x, self.y, 25, 25)
        self.game = game

    def change_position(self):
        self.x = random.randint(0, self.game.screenWidth-25)
        self.y = random.randint(0, self.game.screenHeight-25)
        self.Rect = Rect(self.x, self.y, 25, 25)

    def draw(self, walls):
        for wall in walls:
            if self.x >= wall.x - 25:
                self.change_position()
            if self.x <= wall.x + wall.width:
                self.change_position()
        for wall in walls:
            if self.y >= wall.y - 25:
                self.change_position()
            if self.y <= wall.y + wall.height:
                self.change_position()
        pygame.draw.ellipse(self.game.screen, (255, 0, 0), self.Rect)
