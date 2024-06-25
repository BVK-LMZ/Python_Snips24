import pygame
import sys

# Constants
SCREEN_SIZE = (800, 600)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 36

def initialize_game():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption('Hello Pygame World!')
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def draw_text(screen, text, color, font, position):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=position)
    screen.blit(text_surface, text_rect)

def clear_screen(screen, color):
    screen.fill(color)

def main():
    screen = initialize_game()
    font = pygame.font.Font(None, FONT_SIZE)

    running = True
    while running:
        running = handle_events()

        # Clear the screen
        clear_screen(screen, WHITE)

        # Draw text
        draw_text(screen, 'Hello, Pygame World!', BLACK, font, (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2))

        # Update the screen
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
