import pygame
from player import Player
from constants import *


def main():
    pygame.init()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    clock = pygame.time.Clock() #object to help track the time
    dt = 0
    gameplayer = Player((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))

    print("""Starting Asteroids!
Screen width: 1280
Screen height: 720""")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        updateable.update(dt)
        for items in drawable:
            items.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000 #limiting the loop to 60fps


if __name__ == "__main__":
    main()