# "Graphics/Car.png"
# "Graphics/Car2.png"


import pygame
import random
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
ROAD_WIDTH = int(SCREEN_WIDTH / 1.6)
ROAD_COLOR = (50, 50, 50)
GRASS_COLOR = (60, 220, 0)
LINE_COLOR = (255, 255, 255)
CAR_WIDTH = 50 * 3
CAR_HEIGHT = 100 * 3
CAR_Y = SCREEN_HEIGHT - CAR_HEIGHT - 20  # Y position of the player's car at the bottom of the screen
LINE_WIDTH = 5
CAR_SPEED = 5  # Speed at which car2 moves down
SPAWN_INTERVAL = 5000  # 5 seconds

# Lane positions
LEFT_LANE = (SCREEN_WIDTH - ROAD_WIDTH) / 2 + ROAD_WIDTH / 4 - CAR_WIDTH / 2
RIGHT_LANE = (SCREEN_WIDTH + ROAD_WIDTH) / 2 - ROAD_WIDTH / 4 - CAR_WIDTH / 2

# Initialize the display
pygame.display.set_caption("Car Game")
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Font initialization for displaying text
pygame.font.init()
font = pygame.font.SysFont('Arial', 36)

# Score tracking
score = 0

def draw_road():
    """Draws the road and grass background."""
    display.fill(GRASS_COLOR)  # Fill background with grass color
    road_rect = pygame.Rect((SCREEN_WIDTH - ROAD_WIDTH) / 2, 0, ROAD_WIDTH, SCREEN_HEIGHT)
    pygame.draw.rect(display, ROAD_COLOR, road_rect)  # Draw the main road

def draw_center_line():
    """Draws the center line on the road."""
    line_height = 30
    line_gap = 20
    x = SCREEN_WIDTH / 2 - LINE_WIDTH / 2
    y = 0

    while y < SCREEN_HEIGHT:
        pygame.draw.rect(display, LINE_COLOR, (x, y, LINE_WIDTH, line_height))  # Draw each segment of the center line
        y += line_height + line_gap

def draw_car(display, image_path, x, y):
    """Draws a car on the screen."""
    car_image = pygame.image.load(image_path)  # Load car image
    car_image = pygame.transform.scale(car_image, (CAR_WIDTH, CAR_HEIGHT))  # Scale car image to desired size
    display.blit(car_image, (x, y))  # Blit (draw) car image onto the screen at specified position

def draw_score():
    """Draws the current score at the top left corner."""
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))  # Render score text
    display.blit(score_text, (20, 20))  # Display score text at (20, 20) on the screen

def game_over():
    """Handles the game over screen."""
    global score
    display.fill(GRASS_COLOR)  # Clear screen with grass color
    game_over_text = font.render("GAME OVER", True, (255, 255, 255))  # Render 'GAME OVER' text
    score_text = font.render(f"Final Score: {score}", True, (255, 255, 255))  # Render final score text
    game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))  # Center 'GAME OVER' text
    score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))  # Center final score text
    display.blit(game_over_text, game_over_rect)  # Display 'GAME OVER' text
    display.blit(score_text, score_rect)  # Display final score text

    # Display restart button
    restart_text = font.render("Press R to Restart", True, (255, 0, 0))  # Render 'Press R to Restart' text in red
    restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))  # Center restart text
    display.blit(restart_text, restart_rect)  # Display restart text

    pygame.display.update()  # Update the display to show game over screen

    # Wait for user to press R to restart
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()  # Quit Pygame
                quit()  # Quit Python
            if event.type == KEYDOWN:
                if event.key == K_r:
                    restart_game()  # Restart the game if R key is pressed

def restart_game():
    """Resets the game state and restarts the game."""
    global score
    score = 0  # Reset score to zero
    main()  # Restart the game by calling main()

def main():
    """Main game loop."""
    global score
    running = True
    clock = pygame.time.Clock()
    car_x = LEFT_LANE  # Start in the left lane
    car2_x = random.choice([LEFT_LANE, RIGHT_LANE])  # Randomly choose starting lane for car2
    car2_y = -CAR_HEIGHT  # Start car2 above the screen
    last_spawn_time = pygame.time.get_ticks()  # Track last time a car was spawned

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False  # Quit the game if the window is closed
        
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            car_x = LEFT_LANE  # Move player's car to the left lane
        if keys[K_RIGHT]:
            car_x = RIGHT_LANE  # Move player's car to the right lane

        # Check for car2 spawning
        current_time = pygame.time.get_ticks()
        if current_time - last_spawn_time > SPAWN_INTERVAL:
            car2_x = random.choice([LEFT_LANE, RIGHT_LANE])  # Randomly choose lane for car2
            car2_y = -CAR_HEIGHT  # Start car2 above the screen
            last_spawn_time = current_time  # Update last spawn time
            score += 1  # Increment score when a new car is spawned
        
        # Move car2 down
        car2_y += CAR_SPEED
        
        # Check for collision
        if (car2_x == car_x) and (car2_y + CAR_HEIGHT > CAR_Y) and (car2_y < CAR_Y + CAR_HEIGHT):
            game_over()  # Call game over function if collision occurs

        draw_road()  # Draw the road and background
        draw_center_line()  # Draw the center line on the road
        draw_score()  # Draw the current score
        draw_car(display, "Graphics/Car.png", car_x, CAR_Y)  # Draw the player's car
        draw_car(display, "Graphics/Car2.png", car2_x, car2_y)  # Draw car2
        pygame.display.update()  # Update the display
        
        clock.tick(60)  # Cap the frame rate at 60 frames per second
    
    pygame.quit()  # Quit Pygame when the game loop ends

if __name__ == "__main__":
    main()  # Start the game
