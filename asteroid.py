import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        # 1. Kill this asteroid
        self.kill()
        
        # 2. If radius is too small, just return
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # 3. Spawn 2 new asteroids
        # Generate random angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50)
        
        # Create two new velocity vectors by rotating the current velocity
        new_velocity_1 = self.velocity.rotate(random_angle)
        new_velocity_2 = self.velocity.rotate(-random_angle)
        
        # Compute new radius for smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        # Create two new asteroids at current position
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        
        # Set velocities, scaled up by 1.2 to make them move faster
        asteroid_1.velocity = new_velocity_1 * 1.2
        asteroid_2.velocity = new_velocity_2 * 1.2
