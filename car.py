import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 1920
window_height = 1200
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Racing Game')

# Load the player's car image
car_image = pygame.image.load('car.png')
car_rect = car_image.get_rect()
car_rect.x = window_width / 2
car_rect.y = window_height - 100

# Set up game variables
game_running = True
clock = pygame.time.Clock()
score = 0

# Main game loop
while game_running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    # Handle input
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT]:
        car_rect.x -= 5
    elif keys_pressed[pygame.K_RIGHT]:
        car_rect.x += 5

    # Update game state
    score += 1

    # Draw game elements
    game_window.fill((0, 0, 0))
    game_window.blit(car_image, car_rect)
    pygame.display.flip()

    # Limit frame rate
    clock.tick(60)

# Clean up
pygame.quit()
