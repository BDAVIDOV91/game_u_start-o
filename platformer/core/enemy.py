# core/enemy.py

import pygame
from settings import *
from utils import collide_hit_rect

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        super().__init__()
        self.game = game
        self.image = pygame.Surface((w, h))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hit_rect = self.rect.copy()
        self.vx = 5

    def update(self):
        self.hit_rect.x += self.vx
        self.rect.centerx = self.hit_rect.centerx
        # Check for collisions with platforms
        hits = pygame.sprite.spritecollide(self, self.game.platforms, False, collide_hit_rect)
        if hits:
            self.vx *= -1
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH * 2:
            self.vx *= -1
