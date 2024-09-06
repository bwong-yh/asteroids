import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    
    clock = pygame.time.Clock()
    dt = 0 # second

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    # Group class holds and manages multiple objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    updatable.add(player)
    drawable.add(player)

    running = True
    while running:
        # check if user has closed the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for obj in updatable:
            obj.update(dt)

        screen.fill('black')

        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()

        # pause the loop until 1/60th second has passed - ensure 60 FPS
        # tick() returns the amount of time (ms) last frame took to rendered
        dt = clock.tick(60) / 1000



if __name__ == '__main__':
    main()