import pygame

# screen parameters
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# initialize screen
pygame.init()
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("AKAntiVirus")

background_image = pygame.image.load('antiviruscover.png')
screen.blit(background_image, (0, 0))
pygame.display.flip()

# content to be printed to the screen


run = True
while run:
    screen.blit(background_image, (0, 0))
 
    pygame.display.flip()  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()