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

# timer on screen function
def timer_on_screen(start_ticks, font):
    scan_duration = 9  # total scan time in seconds
    while True:
        screen.fill((0, 0, 0))
        elapsed_seconds = (pygame.time.get_ticks() - start_ticks) // 1000  # calculate elapsed time in seconds
        remaining_seconds = max(scan_duration - elapsed_seconds, 0)  # calculate remaining time
        timer_text = font.render(str(remaining_seconds), True, (255, 255, 255))
        screen.blit(timer_text, (SCREEN_WIDTH // 2 - timer_text.get_width() // 2, SCREEN_HEIGHT // 2 - timer_text.get_height() // 2))
        pygame.display.flip()
        if remaining_seconds <= 0:
            break
        pygame.time.wait(100)

# file scan screen function
def file_scan_screen(file):
    pygame.display.set_caption("scanning a file...")
    font = pygame.font.Font(None, 74)
    title = font.render("Remaining Time: ", True, (255, 255, 255))
    start_ticks = pygame.time.get_ticks()

    scan_thread = Thread(target=av.full_analysis, args=(file,))
    scan_thread.start()

    while scan_thread.is_alive():
        screen.fill((0, 0, 0))  # clear screen before drawing
        screen.blit(title, (50, 50))
        timer_on_screen(start_ticks, font)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                scan_thread.join()  # make sure the scan thread finishes
                pygame.quit()
                return

    scan_thread.join()  # make sure the scan thread finishes
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
            print("Scan file button clicked")
            file_name = scan_file_button.file_prompt()
            print(f"Selected file: {file_name}")
            file_scan_screen(file_name)
        elif scan_directory_button.is_clicked(event):
            print("Scan directory button clicked")

pygame.quit()
