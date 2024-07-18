import pygame

# screen parameters
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# initialize screen
pygame.init()
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("AKAntiVirus")

screen.fill((119, 195, 165))
pygame.display.flip()

# content to be printed to the screen
pygame.font.init()
my_font = pygame.font.SysFont('Adobe', 80)
my_font2 = pygame.font.SysFont('Adobe', 40)  
caption = my_font.render('AKAntiVirus', False, (255, 255, 255))

smaller_text = "Scan your files with over 70 Anti Virus services at once."
lines = ["Scan your files with over 70 Anti", "Virus services at once."]
initial_y = 120

run = True
while run:
    screen.fill((119, 195, 165)) 
    screen.blit(caption, ((SCREEN_WIDTH / 4), 40))
    y = initial_y
    # prints the smaller text to the screen:
    for line in lines:
      smaller_text = my_font2.render(line, False, (255,255,255))
      screen.blit(smaller_text, (50, y))
      y += my_font2.get_height() + 5  

    pygame.display.flip()  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()