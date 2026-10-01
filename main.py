import pygame
import sys
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from powerup import Powerup
from powerupfield import PowerupField
from logger import log_event
from shot import Shot


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: 1280")
    print(f"Screen height: 720")
    
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0.0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    powerups = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    Powerup.containers = (powerups, updatable, drawable)
    PowerupField.containers = (updatable)

    asteroid_field = AsteroidField()
    powerup_field = PowerupField()
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))


    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black", rect = None, special_flags = 0)
        updatable.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
            if asteroid.collides_with(player):
                if player.is_invincible:
                    asteroid.split()
                    log_event("player_hit_blocked")
                else:
                    log_event("player_hit")
                    print("Game Over!")
                    sys.exit()

        for powerup in powerups:
            if powerup.collides_with(player):
                log_event("powerup_collected")
                powerup.apply(player)
                powerup.kill()

        for drawables in drawable:
            drawables.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000




if __name__ == "__main__":
    main()
