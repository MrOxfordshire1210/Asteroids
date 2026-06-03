import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        

    def draw(self, screen: pygame.Surface):
        return pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
        return self.position
    
    def split(self):
        Asteroid.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            rand_angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            fragment1 = Asteroid(self.position[0], self.position[1], new_radius)
            fragment2 = Asteroid(self.position[0], self.position[1], new_radius)
            fragment1.velocity = pygame.Vector2.rotate(self.velocity, rand_angle)*1.2
            fragment2.velocity = pygame.Vector2.rotate(-self.velocity, -rand_angle)*1.2
            
            
