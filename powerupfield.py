import random

import pygame
from constants import (
    POWERUP_SPAWN_RATE_SECONDS,
    POWERUP_DRIFT_SPEED,
    POWERUP_RADIUS,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
)
from powerup import InvincibilityPowerup


class PowerupField(pygame.sprite.Sprite):
    containers: pygame.sprite.Group

    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self) -> None:
        margin = POWERUP_RADIUS * 2
        x = random.uniform(margin, SCREEN_WIDTH - margin)
        y = random.uniform(margin, SCREEN_HEIGHT - margin)
        powerup = InvincibilityPowerup(x, y)
        speed = random.uniform(POWERUP_DRIFT_SPEED * 0.5, POWERUP_DRIFT_SPEED)
        angle = random.uniform(0, 360)
        powerup.velocity = pygame.Vector2(0, 1).rotate(angle) * speed

    def update(self, dt: float) -> None:
        self.spawn_timer += dt
        if self.spawn_timer > POWERUP_SPAWN_RATE_SECONDS:
            self.spawn_timer = 0
            self.spawn()
