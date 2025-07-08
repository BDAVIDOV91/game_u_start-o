# core/enemy.py

import pygame
from settings import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.image = pygame.Surface((w, h))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vx = 5

    def update(self):
        self.rect.x += self.vx
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH * 2:
            self.vx *= -1
