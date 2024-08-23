import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    # MAIN LOOP
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill('black')

        for object in updatable:
            object.update(dt)

        for asteroid in asteroids:
            if asteroid.colliding(player):
                print('Game over!')
                exit()
            for bullet in shots:
                if asteroid.colliding(bullet):
                    asteroid.split()
                    bullet.kill()

        for object in drawable:
            object.draw(screen)

        pygame.display.flip()
        delta = clock.tick(60)
        dt = delta / 1000
        player.update(dt)

if __name__ == "__main__":
    main()
