import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill((0, 255, 0))  # Green for platforms
        self.rect = self.image.get_rect(topleft=pos)