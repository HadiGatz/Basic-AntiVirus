from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askdirectory

import os
import anti_virus as av
from threading import Thread

# get the directory of the current script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESOURCES_PATH = os.path.join(BASE_DIR, "resources")

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

def hide_scan_menu(scanning_text, timer):
    hide_text(scanning_text)
    hide_text(timer)
    scan_done_menu()

def update_timer(timer, time):
    canvas.itemconfig(timer, text=str(time))

def countdown(count, timer, when_finished):
    update_timer(timer, count)
    if count > 0:
        window.after(1000, countdown, count - 1, timer, when_finished) 
    else:
        when_finished()

def scan_menu():
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

    countdown(6, timer, (lambda: hide_scan_menu(scanning_text, timer)))

    

def scan_button_clicked():
    hide_main_menu()
    file = filedialog.askopenfilename(title="Select your file")
    file_scan_thread = Thread(target=av.full_analysis, args=(file,))
    file_scan_thread.start()
    scan_menu()

def scan_done_menu():
    directory_ask = canvas.create_text(
        100,
        401.0,
        anchor="nw",
        text="Pick the directory\n to which the report\n would be exported",
        fill="#FFFFFF",
        font=("Inter Black", 50 * -1)
    )
    directory = askdirectory(title='Select Folder') 
    av.export_analysis(directory, av.report)
    hide_text(directory_ask)
    scan_done = canvas.create_text(
        69.0,
        401.0,
        anchor="nw",
        text="Thanks for using\nour services.",
        fill="#FFFFFF",
        font=("Inter Black", 64 * -1)
    )



button_image_1 = PhotoImage(file=os.path.join(RESOURCES_PATH, "button_1.png"))
button_1 = Button(
    window,
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: scan_button_clicked(),
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
    command=print("clicked"),
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


