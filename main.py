import pygame
import sys

from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from shot import Shot

from tokenize import group
from turtle import update
from constants import PLAYER_RADIUS, SCREEN_HEIGHT
from constants import SCREEN_WIDTH
from logger import log_state
from logger import log_event


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    asteroidfield = AsteroidField()

    while True:
        log_state()

        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collide_with(player) == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for object in drawable:
            object.draw(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
