import pygame
from circleshape import CircleShape
from constants import SHOTS_RADIUS
from constants import LINE_WIDTH


class Shot(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, SHOTS_RADIUS)

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
