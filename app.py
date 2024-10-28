import pygame
import time

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("Minimalist Flip Clock")

# Define fonts and colors
font = pygame.font.Font(None, 80)
bg_color = (0, 0, 0)      # Black background
text_color = (255, 255, 255)  # White text

# Function to update and animate the flip
def draw_time():
    screen.fill(bg_color)
    current_time = time.strftime("%H:%M:%S")
    text = font.render(current_time, True, text_color)
    screen.blit(text, (50, 50))
    pygame.display.flip()

running = True
last_time = ""

# Main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get the current time as a string
    current_time = time.strftime("%H:%M:%S")
    if current_time != last_time:  # Only update on time change
        draw_time()
        last_time = current_time
    time.sleep(0.1)  # Refresh rate to animate seconds

pygame.quit()
