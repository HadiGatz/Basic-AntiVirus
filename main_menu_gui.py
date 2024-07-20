from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askdirectory
import os
import anti_virus as av
from threading import Thread

# get the directory of the current script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESOURCES_PATH = os.path.join(BASE_DIR, "resources")

class Pong:
    def __init__(self, canvas):
        self.canvas = canvas
        self.canvas_width = canvas.winfo_reqwidth()
        self.canvas_height = canvas.winfo_reqheight()
        
        self.board_width = 300
        self.board_height = 150
        self.board_x = (self.canvas_width - self.board_width) // 2
        self.board_y = self.canvas_height - self.board_height - 150
        
        self.paddle_width = 60
        self.paddle_height = 10
        self.paddle_x = self.board_x + (self.board_width - self.paddle_width) // 2
        self.paddle_y = self.board_y + self.board_height - self.paddle_height
        
        self.ball_diameter = 10
        self.ball_x = self.board_x + self.board_width // 2 - self.ball_diameter // 2
        self.ball_y = self.board_y + self.board_height // 2 - self.ball_diameter // 2
        self.ball_speed_x = 4
        self.ball_speed_y = 4

        self.draw_board()
        self.draw_paddle()
        self.draw_ball()
        self.move_ball()

        self.canvas.bind_all('<Left>', self.move_paddle_left)
        self.canvas.bind_all('<Right>', self.move_paddle_right)

    def draw_board(self):
        self.canvas.create_rectangle(self.board_x,
                                     self.board_y,
                                     self.board_x + self.board_width,
                                     self.board_y + self.board_height,
                                     fill="#474AA0",
                                     outline="white")

    def draw_paddle(self):
        self.paddle = self.canvas.create_rectangle(self.paddle_x,
                                                   self.paddle_y,
                                                   self.paddle_x + self.paddle_width,
                                                   self.paddle_y + self.paddle_height,
                                                   fill="white")

    def draw_ball(self):
        self.ball = self.canvas.create_oval(self.ball_x,
                                            self.ball_y,
                                            self.ball_x + self.ball_diameter,
                                            self.ball_y + self.ball_diameter,
                                            fill="white")

    def move_ball(self):
        self.ball_x += self.ball_speed_x
        self.ball_y += self.ball_speed_y
        
        if self.ball_y <= self.board_y or self.ball_y >= self.board_y + self.board_height - self.ball_diameter:
            self.ball_speed_y *= -1
        
        if (self.ball_y + self.ball_diameter >= self.paddle_y and
            self.paddle_x <= self.ball_x <= self.paddle_x + self.paddle_width):
            self.ball_speed_y *= -1

        if self.ball_x <= self.board_x or self.ball_x >= self.board_x + self.board_width - self.ball_diameter:
            self.ball_speed_x *= -1

        if self.ball_y >= self.board_y + self.board_height:
            self.ball_speed_x *= -1
            self.ball_speed_y *= -1
            self.ball_x = self.board_x + self.board_width // 2 - self.ball_diameter // 2
            self.ball_y = self.board_y + self.board_height // 2 - self.ball_diameter // 2

        self.canvas.coords(self.ball, self.ball_x, self.ball_y, self.ball_x + self.ball_diameter, self.ball_y + self.ball_diameter)
        
        self.canvas.after(20, self.move_ball)

    def move_paddle_left(self, event):
        if self.paddle_x > self.board_x:
            self.paddle_x -= 20
            self.canvas.coords(self.paddle, self.paddle_x, self.paddle_y, self.paddle_x + self.paddle_width, self.paddle_y + self.paddle_height)

    def move_paddle_right(self, event):
        if self.paddle_x < self.board_x + self.board_width - self.paddle_width:
            self.paddle_x += 20
            self.canvas.coords(self.paddle, self.paddle_x, self.paddle_y, self.paddle_x + self.paddle_width, self.paddle_y + self.paddle_height)

def hide_rect(rect):
    canvas.itemconfig(rect, state='hidden')

def hide_text(text):
    canvas.itemconfig(text, state='hidden')

def hide_button(button):
    button.place_forget()

window = Tk()
window.geometry("582x682")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=682,
    width=582,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

canvas.create_rectangle(
    0.0,
    192.0,
    582.0,
    682.0,
    fill="#474AA0",
    outline=""
)

title_text = canvas.create_text(
    100,
    201.0,
    anchor="nw",
    text="AK_AntiVirus",
    fill="#FFFFFF",
    font=("Inter Black", 64 * -1)
)

# load the image directly from the "resources" folder
image_path = os.path.join(RESOURCES_PATH, "image_1.png")
if os.path.exists(image_path):
    image_image_1 = PhotoImage(file=image_path)
    image_1 = canvas.create_image(
        291.0,
        96.0,
        image=image_image_1
    )
else:
    print(f"Image not found at path: {image_path}")

explanation_text = canvas.create_text(
    150,
    316.0,
    anchor="nw",
    text="Scanned using 70+\nAnti Virus services",
    fill="#FFFFFF",
    font=("Inter SemiBold", 36 * -1)
)

def hide_main_menu():
    hide_button(button_1)
    hide_button(button_2)
    hide_text(title_text)
    hide_text(explanation_text)
    hide_rect(white_line1)
    hide_rect(white_line2)

def hide_scan_menu(scanning_text, timer, file):
    hide_text(scanning_text)
    hide_text(timer)
    scan_done_menu(file)

def update_timer(timer, time):
    canvas.itemconfig(timer, text=str(time))

def countdown(count, timer, when_finished):
    update_timer(timer, count)
    if count > 0:
        window.after(1000, countdown, count - 1, timer, when_finished) 
    else:
        when_finished()

def scan_menu(file):
    scanning_text = canvas.create_text(
        69.0,
        201.0,
        anchor="nw",
        text="File is Scanned...",
        fill="#FFFFFF",
        font=("Inter Black", 64 * -1)
    )
    
    timer = canvas.create_text(
        69.0,
        401.0,
        anchor="nw",
        text="5",
        fill="#FFFFFF",
        font=("Inter Black", 64 * -1)
    )

    countdown(6, timer, (lambda: hide_scan_menu(scanning_text, timer, file)))

def scan_directory_menu():
    waiting_text = canvas.create_text(
        69.0,
        201.0,
        anchor="nw",
        text="While you wait:",
        fill="#FFFFFF",
        font=("Inter Black", 64 * -1)
    )
    pong = Pong(canvas)

def scan_button_clicked():
    hide_main_menu()
    file = filedialog.askopenfilename(title="Select your file")
    target_directory = askdirectory(title='Where to keep analysis files:')
    file_scan_thread = Thread(target=av.full_analysis, args=(file, target_directory))
    file_scan_thread.start()
    scan_menu(file)

def scan_done_menu(file):
    scan_done = canvas.create_text(
        69.0,
        401.0,
        anchor="nw",
        text="Thanks for using\nour services.",
        fill="#FFFFFF",
        font=("Inter Black", 64 * -1)
    )

def scan_directory_button_clicked():
    hide_main_menu()
    directory = askdirectory(title='Select directory')
    print(".")
    target_directory = askdirectory(title='Where to keep analysis files:')
    directory_scan_thread = Thread(target=av.full_analysis_directory, args=(directory, target_directory))
    directory_scan_thread.start()
    scan_directory_menu()

button_image_1 = PhotoImage(file=os.path.join(RESOURCES_PATH, "button_1.png"))
button_1 = Button(
    window,
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=scan_button_clicked,
    relief="flat"
)
button_1.place(
    x=17.0,
    y=460.0,
    width=271.0,
    height=118.0
)

button_image_hover_1 = PhotoImage(file=os.path.join(RESOURCES_PATH, "button_hover_1.png"))

def button_1_hover(e):
    button_1.config(image=button_image_hover_1)

def button_1_leave(e):
    button_1.config(image=button_image_1)

button_1.bind('<Enter>', button_1_hover)
button_1.bind('<Leave>', button_1_leave)

button_image_2 = PhotoImage(file=os.path.join(RESOURCES_PATH, "button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=scan_directory_button_clicked,
    relief="flat"
)
button_2.place(
    x=291.0,
    y=460.0,
    width=271.0,
    height=118.0
)

button_image_hover_2 = PhotoImage(file=os.path.join(RESOURCES_PATH, "button_hover_2.png"))

def button_2_hover(e):
    button_2.config(image=button_image_hover_2)

def button_2_leave(e):
    button_2.config(image=button_image_2)

button_2.bind('<Enter>', button_2_hover)
button_2.bind('<Leave>', button_2_leave)

white_line1 = canvas.create_rectangle(
    117.0,
    304.0,
    466.0,
    309.0,
    fill="#FFFFFF",
    outline=""
)

white_line2 = canvas.create_rectangle(
    117.0,
    413.0,
    466.0,
    418.0,
    fill="#FFFFFF",
    outline=""
)

window.resizable(False, False)
window.mainloop()
