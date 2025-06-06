import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):

    def __init__(self, x: int, y: int, radius: int):
        super().__init__(x, y, radius)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
