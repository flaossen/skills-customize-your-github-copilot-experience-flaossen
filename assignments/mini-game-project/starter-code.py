import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mini Game Project")

clock = pygame.time.Clock()

player_x = 100
player_y = 450
player_speed = 5
player_size = 30

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    player_x = max(0, min(player_x, SCREEN_WIDTH - player_size))
    player_y = max(0, min(player_y, SCREEN_HEIGHT - player_size))

    screen.fill((20, 20, 30))
    pygame.draw.rect(screen, (50, 180, 255), (player_x, player_y, player_size, player_size))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
