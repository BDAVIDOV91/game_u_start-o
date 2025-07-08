import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, speed):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill((0, 0, 255)) # Blue square for enemy
        self.rect = self.image.get_rect(topleft=pos)
        self.speed = speed
        self.direction = 1 # 1 for right, -1 for left

    def move(self):
        self.rect.x += self.speed * self.direction

    def reverse_direction(self):
        self.direction *= -1

    def check_platform_edge(self, platforms):
        # Check one pixel below the current position to see if there's ground
        # And check one pixel ahead in the current direction
        check_pos_x = self.rect.centerx + (self.direction * (self.rect.width // 2 + 1))
        check_pos_y = self.rect.bottom + 1

        # Create a small rect to check for collision at the edge
        edge_rect = pygame.Rect(check_pos_x - 1, check_pos_y, 2, 1) # 2x1 pixel rect

        on_platform = False
        for platform in platforms:
            if platform.rect.colliderect(edge_rect):
                on_platform = True
                break

        if not on_platform:
            self.reverse_direction()

    def update(self, platforms):
        self.move()
        self.check_platform_edge(platforms)
