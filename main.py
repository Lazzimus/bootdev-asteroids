import pygame
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from logger import log_state

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: 1280")
    print(f"Screen height: 720")
    
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT
                return
        screen.fill("black", rect = None, special_flags = 0)
        pygame.display.flip()



if __name__ == "__main__":
    main()
