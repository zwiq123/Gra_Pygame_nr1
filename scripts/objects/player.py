from scripts.utils.constants import *
from .gameObject import *


class Player(GameObject):
    def __init__(self, x, y, game):
        super().__init__(x, y, 50, 50, game)
        super().set_color((255, 255, 0))
        self.xVel = 0
        self.yVel = 0
        self.speed = 0.5
        self.points = 0

    def update(self):
        if self.points >= 1000:
            self.speed = 0.8
            self.width = 75
            self.height = 75

        self.yVel += GRAVITY
        self.xVel *= (1 - RESISTANCE)
        self.yVel *= (1 - RESISTANCE)

        self.solve_collisions(self.game.levelManager.walls)

        super().update()

    def draw(self, offset):
        super().draw(offset)

    def solve_collisions(self, walls):
        self.x += self.xVel
        self.Rect = Rect(self.x, self.y, self.width, self.height)
        for wall in walls:
            if self.Rect.colliderect(wall.Rect):
                if self.xVel > 0:
                    self.x = wall.x - self.width
                    if wall.isBouncy:
                        self.xVel *= -1.5
                        self.x += self.xVel
                    else:
                        self.xVel = 0
                elif self.xVel < 0:
                    self.x = wall.x + wall.width
                    if wall.isBouncy:
                        self.xVel *= -1.5
                        self.x += self.xVel
                    else:
                        self.xVel = 0
            self.Rect = Rect(self.x, self.y, self.width, self.height)

        self.y += self.yVel
        self.Rect = Rect(self.x, self.y, self.width, self.height)
        for wall in walls:
            if self.Rect.colliderect(wall.Rect):
                if self.yVel > 0:
                    self.y = wall.y - self.height
                    if wall.isBouncy:
                        self.yVel *= -1.5
                        self.y += self.yVel
                    else:
                        self.yVel = 0
                elif self.yVel < 0:
                    self.y = wall.y + wall.height
                    if wall.isBouncy:
                        self.yVel *= -1.5
                        self.y += self.yVel
                    else:
                        self.yVel = 0
            self.Rect = Rect(self.x, self.y, self.width, self.height)
