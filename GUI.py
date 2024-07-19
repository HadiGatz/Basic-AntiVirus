import pygame

# Screen parameters
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Initialize screen
pygame.init()
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("AKAntiVirus")

# Load background image
background_image = pygame.image.load('antiviruscover.png')

# Button class
class Button:
    def __init__(self, x, y, width=200, height=120):
        self.rect = pygame.Rect(x, y, width, height)

    def is_clicked(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                print("clicked")

# Create button instances
scan_file_button = Button(50, 410)
scan_directory_button = Button(450, 410)

# Main loop
run = True
while run:
    screen.blit(background_image, (0, 0))
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif scan_file_button.is_clicked():
            print("Scan File Button Clicked")
        elif scan_directory_button.is_clicked():
            print("Scan Directory Button Clicked")

pygame.quit()
