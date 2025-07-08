# core/level.py

import pygame
from settings import *
from core.platform import Platform

class Level:
    def __init__(self, file_path):
        self.platforms = []
        with open(file_path, 'r') as f:
            for y, line in enumerate(f):
                for x, char in enumerate(line):
                    if char == 'P':
                        self.platforms.append(Platform(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    def add_sprites(self, group):
        for p in self.platforms:
            group.add(p)
