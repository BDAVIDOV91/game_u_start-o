# core/player.py

import pygame
from settings import *
from utils import collide_hit_rect

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        super().__init__()
        self.game = game
        self.load_images()
        self.image = self.idle_frames[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hit_rect = self.rect
        self.vel = pygame.math.Vector2(0, 0)
        self.acc = pygame.math.Vector2(0, 0)
        self.on_ground = False
        self.walking = False
        self.current_frame = 0
        self.last_update = 0

    def load_images(self):
        self.idle_frames = [pygame.image.load("platformer/assets/images/player/idle.png").convert()]
        for frame in self.idle_frames:
            frame.set_colorkey(BLACK)
        self.walk_frames_r = [
            pygame.image.load("/home/technojihad/game_u_start-o/platformer/assets/images/player/walk1.png").convert(),
            pygame.image.load("/home/technojihad/game_u_start-o/platformer/assets/images/player/walk2.png").convert()
        ]
        self.walk_frames_l = []
        for frame in self.walk_frames_r:
            frame.set_colorkey(BLACK)
            self.walk_frames_l.append(pygame.transform.flip(frame, True, False))

    def update(self):
        self.animate()
        self.acc = pygame.math.Vector2(0, PLAYER_GRAVITY)
        self.walking = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acc.x = -PLAYER_ACC
            self.walking = True
        if keys[pygame.K_RIGHT]:
            self.acc.x = PLAYER_ACC
            self.walking = True

        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        self.hit_rect.x += self.vel.x + 0.5 * self.acc.x
        self.hit_rect.y += self.vel.y
        self.rect.center = self.hit_rect.center

    def animate(self):
        now = pygame.time.get_ticks()
        if self.walking:
            if now - self.last_update > 200:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.walk_frames_l)
                if self.vel.x > 0:
                    self.image = self.walk_frames_r[self.current_frame]
                else:
                    self.image = self.walk_frames_l[self.current_frame]
        else:
            self.image = self.idle_frames[0]

    def jump(self):
        # jump only if standing on a platform
        self.rect.y += 1
        hits = pygame.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.y -= 1
        if hits:
            self.vel.y = -PLAYER_JUMP

    def draw(self, surface):
        surface.blit(self.image, self.rect)
