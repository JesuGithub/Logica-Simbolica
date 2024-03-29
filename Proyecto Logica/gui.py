
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\j2a0a\OneDrive\Documentos\Progra\Logica Simbolica\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("1440x1045")
window.configure(bg = "#EBF8FF")

# Listas

lista_universal = []
lista_A = []
lista_B = []
lista_C = []
lista_D = []

# Funciones

def separarLista(texto):
    texto_separado = texto.split(",")

canvas = Canvas(
    window,
    bg = "#EBF8FF",
    height = 1045,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    77.0,
    131.0,
    anchor="nw",
    text="Conjunto Universal\n",
    fill="#61A146",
    font=("Inter", 28 * -1)
)

# Entrys

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    368.0,
    212.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=97.0,
    y=182.0,
    width=542.0,
    height=58.0
)

# Entry 2

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    366.0,
    365.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=95.0,
    y=335.0,
    width=542.0,
    height=58.0
)

# Entry 3

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    1089.0,
    365.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=818.0,
    y=335.0,
    width=542.0,
    height=58.0
)

# Entry 4

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    366.0,
    610.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=95.0,
    y=580.0,
    width=542.0,
    height=58.0
)

# Entry 5

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    710.0,
    855.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=439.0,
    y=825.0,
    width=542.0,
    height=58.0
)

# Entry 6

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    1089.0,
    610.0,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=818.0,
    y=580.0,
    width=542.0,
    height=58.0
)

# Configurar la fuente del Entry
entry_1.config(font=("Roboto", 20))
entry_2.config(font=("Roboto", 20))
entry_3.config(font=("Roboto", 20))
entry_4.config(font=("Roboto", 20))
entry_5.config(font=("Roboto", 20))
entry_6.config(font=("Roboto", 20))

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
    x=798.0,
    y=182.0,
    width=230.0,
    height=65.0
)

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
    x=1089.0,
    y=825.0,
    width=230.0,
    height=65.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=1090.0,
    y=24.0,
    width=230.0,
    height=65.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=766.0,
    y=24.0,
    width=253.0,
    height=65.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=419.0,
    y=24.0,
    width=276.0,
    height=65.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=118.0,
    y=24.0,
    width=230.0,
    height=65.0
)

canvas.create_text(
    75.0,
    284.0,
    anchor="nw",
    text="Subconjunto A",
    fill="#61A146",
    font=("Inter", 28 * -1)
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=75.0,
    y=411.0,
    width=230.0,
    height=65.0
)

canvas.create_text(
    798.0,
    284.0,
    anchor="nw",
    text="Subconjunto B",
    fill="#61A146",
    font=("Inter", 28 * -1)
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=798.0,
    y=411.0,
    width=230.0,
    height=65.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)
button_9.place(
    x=75.0,
    y=656.0,
    width=230.0,
    height=65.0
)

canvas.create_text(
    75.0,
    529.0,
    anchor="nw",
    text="Subconjunto A",
    fill="#61A146",
    font=("Inter", 28 * -1)
)

canvas.create_text(
    618.0,
    773.0,
    anchor="nw",
    text="Subconjunto A",
    fill="#61A146",
    font=("Inter", 28 * -1)
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_10 clicked"),
    relief="flat"
)
button_10.place(
    x=514.0,
    y=941.0,
    width=411.0,
    height=65.0
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_11 clicked"),
    relief="flat"
)
button_11.place(
    x=798.0,
    y=656.0,
    width=230.0,
    height=65.0
)

canvas.create_text(
    798.0,
    529.0,
    anchor="nw",
    text="Subconjunto B",
    fill="#61A146",
    font=("Inter", 28 * -1)
)

window.resizable(False, False)
window.mainloop()
