from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event
import pygame
import random
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float):
        self.position += (self.velocity * dt)

    def split(self):
        old_radius = self.radius
        x = self.position.x
        y = self.position.y

        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)
            velocity1 = self.velocity.rotate(random_angle)
            velocity2 = (self.velocity.rotate(-random_angle))
            split_radius = old_radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(x, y, split_radius)
            asteroid2 = Asteroid(x, y, split_radius)
            asteroid1.velocity = (velocity1 * 1.2)
            asteroid2.velocity = (velocity2 * 1.2)
