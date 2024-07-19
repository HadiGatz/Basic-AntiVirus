import pygame
import tkinter
import tkinter.filedialog
import time
from threading import Thread
import anti_virus as av

# screen parameters
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# initialize screen
pygame.init()
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("AKAntiVirus")

# load background image
background_image = pygame.image.load('antiviruscover.png')

# button class
class Button:
    def __init__(self, x, y, width=200, height=120):
        self.rect = pygame.Rect(x, y, width, height)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False

class FileButton(Button):
    def __init__(self, x, y, width=200, height=120):
        Button.__init__(self, x, y, width, height)

    def file_prompt(self):
        top = tkinter.Tk()
        top.withdraw()  # hide window
        file_name = tkinter.filedialog.askopenfilename(parent=top)
        top.destroy()
        return file_name

# create button instances
scan_file_button = FileButton(50, 410)
scan_directory_button = Button(350, 410)

# dummy scan function
def dummy_scan_function():
    time.sleep(5)  # simulate a scan that takes 5 seconds

def timer_on_screen(start_ticks, font):
    screen.fill((0, 0, 0))
    seconds = (pygame.time.get_ticks() - start_ticks) // 1000  # calculate elapsed time in seconds
    timer_text = font.render(str(seconds), True, (255, 255, 255))
    screen.blit(timer_text, (SCREEN_WIDTH // 2 - timer_text.get_width() // 2, SCREEN_HEIGHT // 2 - timer_text.get_height() // 2))
    pygame.display.flip()

def file_scan_screen(file):
    pygame.display.set_caption("scanning a file...") 
    font = pygame.font.Font(None, 74)
    start_ticks = pygame.time.get_ticks()
    
    scan_thread = Thread(target=av.full_analysis, args=(file,))
    scan_thread.start()

    run = True
    while run:
        timer_on_screen(start_ticks, font)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if not scan_thread.is_alive():
            run = False

    scan_thread.join()
    # after scanning is done
    pygame.display.set_caption("AKAntiVirus")

# main loop
run = True
while run:
    screen.blit(background_image, (0, 0))
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif scan_file_button.is_clicked(event):
            print("scan file button clicked")
            file_name = scan_file_button.file_prompt()
            print(f"selected file: {file_name}")
            file_scan_screen(file_name)
        elif scan_directory_button.is_clicked(event):
            print("scan directory button clicked")

pygame.quit()
