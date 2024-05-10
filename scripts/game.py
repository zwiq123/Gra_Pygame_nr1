import os
import pygame
from pygame.locals import *
from objects.player import Player
from utils.constants import *
from managers.levelManager import LevelManager
from managers.offsetManager import OffsetManager


class Game:
    def __init__(self):
        pygame.init()
        self.screenWidth = SCREEN_WIDTH
        self.screenHeight = SCREEN_HEIGHT
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 24)
        self.mouseX, self.mouseY = (0, 0)
        self.offsetManager = OffsetManager((0, 0), 0.1)
        self.player1 = Player(100, 100, self)
        self.coins = []
        self.levelManager = LevelManager(self)
        self.running = False
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        self.music = pygame.mixer.Sound("sounds/thesis.ogg")
        self.music.set_volume(0.01)

        if os.path.exists("level.txt"):
            self.levelManager.level = self.levelManager.read_level("level.txt")
            self.levelManager.add_walls()
            self.levelManager.add_enemies()
        self.game_loop()


    def game_loop(self):
        self.running = True
        self.music.play()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    break

            self.key_manager()
            self.mouse_and_offset_manager()
            self.draw_manager()
            self.point_manager()

            self.clock.tick(60)
            pygame.display.flip()
        pygame.quit()
        self.levelManager.save_level("level.txt")

    def draw_manager(self):
        self.screen.fill((0, 0, 0))
        offset = self.offsetManager.get_offset()
        for wall in self.levelManager.walls:
            wall.draw(offset)
        # for enemy in self.levelManager.enemies:
        #     enemy.draw(offset)
        self.player1.draw(offset)

    def mouse_and_offset_manager(self):
        self.mouseX, self.mouseY = pygame.mouse.get_pos()
        targetOffset = (self.player1.Rect.centerx - SCREEN_WIDTH // 2 + (self.mouseX - SCREEN_WIDTH // 2) / 2,
                        self.player1.Rect.centery - SCREEN_HEIGHT // 2 + (self.mouseY - SCREEN_HEIGHT // 2) / 2)
        self.offsetManager.updateOffset(targetOffset)

    def point_manager(self):
        for coin in self.coins:
            if self.player1.Rect.colliderect(coin.Rect):
                coin.change_position()
                self.player1.points += 1

        self.screen.blit(self.font.render(f'x: {str(self.player1.x.__round__(0)).split(".")[0]},  y: {str(self.player1.y.__round__(0)).split(".")[0]}', True, (255, 255, 255)), (5, 5))

        textL = self.font.render(f'points: ', True, (255, 255, 255))
        if self.player1.points >= 1000:
            textV = self.font.render(f'{self.player1.points}', True, (255, 0, 255))
            self.screen.blit(textL, (self.player1.xDraw - 10, self.player1.yDraw - 30))
            self.screen.blit(textV, (self.player1.xDraw + 50, self.player1.yDraw - 30))
        else:
            textV = self.font.render(f'{self.player1.points}', True, (0, 255, 255))
            self.screen.blit(textL, (self.player1.xDraw - 15, self.player1.yDraw - 30))
            self.screen.blit(textV, (self.player1.xDraw + 45, self.player1.yDraw - 30))

    def key_manager(self):
        keys = pygame.key.get_pressed()
        if keys[K_w]:
            self.player1.yVel -= self.player1.speed
        if keys[K_s]:
            self.player1.yVel += self.player1.speed
        if keys[K_a]:
            self.player1.xVel -= self.player1.speed
        if keys[K_d]:
            self.player1.xVel += self.player1.speed
        self.player1.update()

