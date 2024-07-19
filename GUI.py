import pygame
import tkinter
import tkinter.filedialog
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

    def is_clicked(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                return True

class FileButton(Button):
    def __init__(self, x, y, width=200, height=120):
        Button.__init__(self, x, y, width, height)

    def file_prompt(self):
        top = tkinter.Tk()
        top.withdraw()  
        file_name = tkinter.filedialog.askopenfilename(parent=top)
        top.destroy()
        return file_name

# create button instances
scan_file_button = FileButton(50, 410)
scan_directory_button = Button(350, 410)

# main loop
run = True
while run:
    screen.blit(background_image, (0, 0))
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif scan_file_button.is_clicked():
            print("Scan File Button Clicked")
            file = scan_file_button.file_prompt()
            av.check_if_corrupted(file)
            response = av.scan_file(file)
            scan_results = dict(response.json())
            scan_url = scan_results['data']['links']['self']
            analysis = av.retrieve_scan_results(scan_url)
            av.print_analysis_results(analysis.json()['data']['attributes']['stats'])      

        elif scan_directory_button.is_clicked():
            print("Scan Directory Button Clicked")

pygame.quit()
