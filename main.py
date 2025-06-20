import pygame, sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialise pygame
    pygame.init()

    # Create the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Create sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Set up Asteroid containers
    Asteroid.containers = (asteroids, updatable, drawable)

    # Set up AsteroidField containers (only updatable, not drawable)
    AsteroidField.containers = (updatable,)

    # Create player instance after filling the screen but before flipping the display
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    updatable.add(player)
    drawable.add(player)

    # Create AsteroidField instance
    asteroid_field = AsteroidField()

    # Basic game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Fill the screen with black
        screen.fill("black")

        # Update all updatable objects
        updatable.update(dt)

        # Draw all drawable objects
        for sprite in drawable:
            sprite.draw(screen)

        # Check for collisions between player and asteroids
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                sys.exit()

        # Refresh the screen
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
