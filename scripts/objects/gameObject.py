from pygame.locals import *
import pygame

class GameObject:
    def __init__(self, x, y, width, height, imgSrc, game):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.Rect = Rect(self.x, self.y, self.width, self.height)
        self.xDraw = 0
        self.yDraw = 0
        self.game = game
        self.color = (255, 0, 0)
        if imgSrc is not None:
            self.img = pygame.transform.scale(pygame.image.load(imgSrc), (self.width, self.height))
        else:
            self.img = None

    def set_color(self, color):
        self.color = color

    def update(self):
        self.Rect = Rect(self.x, self.y, self.width, self.height)

    def draw(self, offset):
        self.xDraw = self.x - offset[0]
        self.yDraw = self.y - offset[1]
        drawRect = Rect(self.x - offset[0], self.y - offset[1], self.width, self.height)

        if self.img is not None:
            self.game.screen.blit(self.img, (self.xDraw, self.yDraw))
        else:
            pygame.draw.rect(self.game.screen, self.color, drawRect)
