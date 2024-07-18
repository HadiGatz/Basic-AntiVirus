import pygame

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

pygame.init()
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("AKAntiVirus")

screen.fill((119, 195, 165))
pygame.display.flip()

pygame.font.init()
my_font = pygame.font.SysFont('Adobe', 80)  # Increased font size to 60
text_surface = my_font.render('AKAntiVirus', False, (255, 255, 255))

run = True
while run:
    screen.fill((119, 195, 165)) 
    screen.blit(text_surface, ((SCREEN_WIDTH / 4), 40))  
    pygame.display.flip()  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()