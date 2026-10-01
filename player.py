import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_SHOOT_COOLDOWN_SECONDS
from constants import LINE_WIDTH
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED
from constants import PLAYER_SHOOT_SPEED
from constants import INVINCIBILITY_DURATION_SECONDS, INVINCIBILITY_FLASH_HZ
from logger import log_event
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.x = x
        self.y = y
        self.PLAYER_RADUS = PLAYER_RADIUS
        self.rotation = 0
        self.cooldown = 0
        self.invincibility_timer = 0.0


        # in the Player class
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]


    def draw(self, screen: pygame.Surface) -> None:
        if self.is_invincible and self._flash_hidden():
            return
        color = "cyan" if self.is_invincible else "white"
        pygame.draw.polygon(screen, color, self.triangle(), LINE_WIDTH)


    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt


    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()
        self.cooldown -= dt

        if self.invincibility_timer > 0:
            self.invincibility_timer -= dt
            if self.invincibility_timer < 0:
                self.invincibility_timer = 0

        if keys[pygame.K_a]:
            self.rotate(-abs(dt))
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-abs(dt))
        if keys[pygame.K_SPACE]:
            if self.cooldown > 0:
                pass
            else:
                self.shoot()
                self.cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

    @property
    def is_invincible(self) -> bool:
        return self.invincibility_timer > 0

    def activate_invincibility(self) -> None:
        self.invincibility_timer = INVINCIBILITY_DURATION_SECONDS
        log_event("invincibility_activated")

    def _flash_hidden(self) -> bool:
        """Makes the ship blink while invincible so the state is visible."""
        return int(self.invincibility_timer * INVINCIBILITY_FLASH_HZ) % 2 == 0
