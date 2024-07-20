from tkinter import *
import os

# get the directory of the current script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESOURCES_PATH = os.path.join(BASE_DIR, "resources")



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

canvas.create_text(
    69.0,
    201.0,
    anchor="nw",
    text="Scanning File",
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





window.resizable(False, False)
window.mainloop()
