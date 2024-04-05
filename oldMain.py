# Potrzebne importy
import pygame
from pygame.locals import *

# Inicjalizacja wszystkich mechanizmów pythona (po prostu to jest ważne);
pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
# Parametry Screena
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Zegar kontrolujący FPS-y
clock = pygame.time.Clock()

x = 100
y = 100
speed = 0.5
shape = 1

xVel = 0
yVel = 0
GRAVITY = 1
RESISTANCE = 0.02

width = 50
height = 50


# Pętla gry
running = True
while running:

    # Te cztery linijki pozwalają nam normalnie zamknąć program.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    keys = pygame.key.get_pressed()

    if not keys[K_w]:
        yVel += GRAVITY

    if keys[K_d]:
        xVel += speed
    if keys[K_a]:
        xVel -= speed
    if keys[K_w]:
        yVel -= speed
    if keys[K_s]:
        yVel += speed

    xVel *= (1 - RESISTANCE)
    yVel *= (1 - RESISTANCE)

    x += xVel
    y += yVel

    if x < 0:
        x = 0
        xVel *= -0.5
    if x > SCREEN_WIDTH - width:
        x = SCREEN_WIDTH - width
        xVel *= -0.5
    if y < 0:
        y = 0
        yVel = 0
    if y > SCREEN_HEIGHT - height:
        y = SCREEN_HEIGHT - height
        yVel *= -0.5

    # Rysowanie grafiki:

    # Wypełnienie okienka kolorem
    screen.fill((0, 0, 0))

    # Rysowanie kształtu
    if keys[K_q]:
        shape = 1
    if keys[K_e]:
        shape = 2

    if shape == 1:
        if xVel >= 0:
            if yVel >= 0:
                pygame.draw.rect(screen, (255, 255, 0), Rect(x, y, 50 + (xVel + 1), 50 + (yVel + 1)))
            else:
                pygame.draw.rect(screen, (255, 255, 0), Rect(x, (y + 1) + yVel, 50 + (xVel + 1), 50))
        else:
            if yVel >= 0:
                pygame.draw.rect(screen, (255, 255, 0), Rect(x + xVel, y, 50, 50 + (yVel + 1)))
            else:
                pygame.draw.rect(screen, (255, 255, 0), Rect(x + xVel, (y + 1) + yVel, 50, 50))
    elif shape == 2:
        pygame.draw.ellipse(screen, (255, 255, 0), Rect(x, y, 50*(xVel+1), 50*(yVel+1)))
    else:
        pygame.draw.rect(screen, (255, 255, 0), Rect(x, y, 50*(xVel+1), 50*(yVel+1)))

    pygame.draw.ellipse(screen, (255, 255, 0), Rect(100, 300, 50, 50))
    pygame.draw.aaline(screen, (255, 0, 0), (50, 50), (1000, 1000))

    # Czekanie na kolejną klatkę
    clock.tick(60)
    # Aktualizacja gry
    pygame.display.flip()

pygame.quit()
