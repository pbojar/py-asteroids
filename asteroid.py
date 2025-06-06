import pygame
import random
from circleshape import CircleShape
from constants import *

def split_spawn(old_position, old_velocity, old_radius, split_angle):
    new_radius = old_radius - ASTEROID_MIN_RADIUS
    asteroid = Asteroid(*old_position, new_radius)
    asteroid.velocity = 1.2 * old_velocity.rotate(split_angle)

class Asteroid(CircleShape):

    def __init__(self, x: int, y: int, radius: int):
        super().__init__(x, y, radius)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            angle = random.uniform(20, 50)
            split_spawn(self.position, self.velocity, self.radius, angle)
            split_spawn(self.position, self.velocity, self.radius, -angle)

