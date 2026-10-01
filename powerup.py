import pygame
from circleshape import CircleShape
from constants import POWERUP_RADIUS, LINE_WIDTH


class Powerup(CircleShape):
    """Base class for pickups that drift around the screen and expire
    after a while if the player doesn't grab them."""

    LIFETIME_SECONDS = 10.0

    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, POWERUP_RADIUS)
        self.age = 0.0

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
        self.age += dt
        if self.age >= self.LIFETIME_SECONDS:
            self.kill()

    def draw(self, screen: pygame.Surface) -> None:
        # must override
        pass

    def apply(self, player) -> None:
        """Apply this powerup's effect to the player. Override in subclasses."""
        pass


class InvincibilityPowerup(Powerup):
    """A shield pickup that grants the player temporary invincibility."""

    def draw(self, screen: pygame.Surface) -> None:
        pos = (int(self.position.x), int(self.position.y))
        # Cyan ring so it reads clearly as a shield/shield pickup
        pygame.draw.circle(screen, "cyan", pos, int(self.radius), LINE_WIDTH)
        pygame.draw.circle(screen, "cyan", pos, int(self.radius * 0.45), LINE_WIDTH)

    def apply(self, player) -> None:
        player.activate_invincibility()
