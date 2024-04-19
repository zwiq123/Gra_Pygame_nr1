from .gameObject import GameObject
import pygame


class Wall(GameObject):
    def __init__(self, x, y, width, height, game):
        super().__init__(x, y, width, height, "textures/cobble.png", game)
        self.isBouncy = False
        super().set_color((128, 128, 128))

    def set_bouncy(self):
        self.isBouncy = True
        super().set_color((0, 128, 0))
        self.img = pygame.transform.scale(pygame.image.load("textures/slime_block.png"), (self.width, self.height))

    def draw(self, offset):
        super().draw(offset)
