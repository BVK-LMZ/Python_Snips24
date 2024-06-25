#cool loading screen 
#needs Graphics/Star

import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Create the Pygame display surface
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Loading Screen Example")

# Load the star image from file
star_image = pygame.image.load('Graphics/Star.png')

# Coordinates for displaying stars in the corner
star_x = 10
star_y = screen_height - 50

# Function to handle quit event
def handle_quit_event():
    pygame.quit()  # Close Pygame
    sys.exit()     # Exit the program



# Function to display stars sequentially
def display_loading_screen():
    clock = pygame.time.Clock()  # Create a clock to control frame rate

    # Display star 1
    screen.blit(star_image, (star_x, star_y))  # Draw star at specified coordinates
    pygame.display.flip()  # Update the screen
    clock.tick(2)  # Wait for 2 frames (approx. 0.067 seconds at 30 FPS)

    # Display star 2
    screen.blit(star_image, (star_x + 50, star_y))  # Offset star by 50 pixels
    pygame.display.flip()  # Update the screen
    clock.tick(2)  # Wait for 2 frames

    # Display star 3
    screen.blit(star_image, (star_x + 100, star_y))  # Offset star by 100 pixels
    pygame.display.flip()  # Update the screen
    clock.tick(2)  # Wait for 2 frames

    # Wait before clearing stars
    clock.tick(45)  # Wait for 45 frames (approx. 1.5 seconds at 30 FPS)
    screen.fill((0, 0, 0))  # Clear the screen (fill with black)
    pygame.display.flip()  # Update the screen to clear stars

# Function to handle events
def handle_events(last_input):
    for event in pygame.event.get():  # Iterate through all Pygame events
        if event.type == pygame.QUIT:  # Check if 'QUIT' event (window close)
            handle_quit_event()  # Call function to quit the program
        else:
            pass
    return last_input

# Main function
def main():
    clock = pygame.time.Clock()  # Create a clock object to manage time
    running = True  # Flag to control main loop
    last_input = ""  # Initialize variable to store user input

    while running:
        last_input = handle_events(last_input)  # Handle events each iteration
        # Display loading screen with stars
        display_loading_screen()

        # Cap the frame rate (adjust as needed)
        clock.tick(30)  # Limit FPS to 500 (approx. 500 frames per second)

if __name__ == '__main__':
    main()  # Run the main function if this script is executed directly
