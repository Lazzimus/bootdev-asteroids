import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen) -> None:
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), int(self.radius), SHOT_RADIUS)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
