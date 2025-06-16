import pygame
from constants import *
from player import Player

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
    # Create player instance after filling the screen but before flipping the display
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    # Basic game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Fill the screen with black
        screen.fill("black")

        # Update the player (handle input and rotation)
        player.update(dt)

        # Draw the player
        player.draw(screen)
        # Refresh the screen
        pygame.display.flip()
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
