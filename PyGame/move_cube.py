import pygame
import sys



# Initialize Pygame
pygame.init()

# Screen setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pygame Player Example')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define the Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill(WHITE)
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Keep player within screen boundaries
        self.rect.clamp_ip(screen.get_rect())

# Create an instance of Player
player = Player()

# Clock setup
clock = pygame.time.Clock()
fps = 60

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Get all the keys currently pressed
    pressed_keys = pygame.key.get_pressed()

    # Update the player sprite based on user keypresses
    player.update(pressed_keys)

    # Fill the screen with black
    screen.fill(BLACK)

    # Draw the player onto the screen
    screen.blit(player.surf, player.rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(fps)

# Clean up and quit
pygame.quit()
sys.exit()
