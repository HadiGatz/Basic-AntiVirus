

from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\User\Desktop\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("582x682")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 682,
    width = 582,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    192.0,
    582.0,
    682.0,
    fill="#474AA0",
    outline="")

canvas.create_text(
    69.0,
    201.0,
    anchor="nw",
    text="AK_AntiVirus",
    fill="#FFFFFF",
    font=("Inter Black", 64 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    291.0,
    96.0,
    image=image_image_1
)

canvas.create_text(
    121.0,
    316.0,
    anchor="nw",
    text="Scanned using 70+\nAnti Virus services",
    fill="#FFFFFF",
    font=("Inter SemiBold", 36 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=17.0,
    y=460.0,
    width=271.0,
    height=118.0
)

button_image_hover_1 = PhotoImage(
    file=relative_to_assets("button_hover_1.png"))

def button_1_hover(e):
    button_1.config(
        image=button_image_hover_1
    )
def button_1_leave(e):
    button_1.config(
        image=button_image_1
    )

button_1.bind('<Enter>', button_1_hover)
button_1.bind('<Leave>', button_1_leave)


button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=291.0,
    y=460.0,
    width=271.0,
    height=118.0
)

button_image_hover_2 = PhotoImage(
    file=relative_to_assets("button_hover_2.png"))

def button_2_hover(e):
    button_2.config(
        image=button_image_hover_2
    )
def button_2_leave(e):
    button_2.config(
        image=button_image_2
    )

button_2.bind('<Enter>', button_2_hover)
button_2.bind('<Leave>', button_2_leave)


canvas.create_rectangle(
    117.0,
    304.0,
    466.0,
    309.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    117.0,
    413.0,
    466.0,
    418.0,
    fill="#FFFFFF",
    outline="")
window.resizable(False, False)
window.mainloop()
