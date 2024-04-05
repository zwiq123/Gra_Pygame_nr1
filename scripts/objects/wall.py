from .gameObject import GameObject


class Wall(GameObject):
    def __init__(self, x, y, width, height, game):
        super().__init__(x, y, width, height, None, game)
        self.isBouncy = False
        super().set_color((128, 128, 128))

    def set_bouncy(self):
        self.isBouncy = True
        super().set_color((0, 128, 0))

    def draw(self, offset):
        super().draw(offset)
