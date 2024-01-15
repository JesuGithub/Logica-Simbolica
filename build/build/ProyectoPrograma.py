from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\j2a0a\OneDrive\Documentos\Progra\Logica Simbolica\build\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1440x1045")
window.configure(bg = "#F3F6F4")


canvas = Canvas(
    window,
    bg = "#F3F6F4",
    height = 1045,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
boton_eliminar_image = PhotoImage(
    file=relative_to_assets("button_1.png"))
boton_eliminar = Button(
    image=boton_eliminar_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: quitar_texto(),
    relief="flat"
)
boton_eliminar.place(
    x=1089.0,
    y=825.0,
    width=230.0,
    height=65.0
)

boton_diferencia_image = PhotoImage(
    file=relative_to_assets("button_2.png"))
boton_diferencia = Button(
    image=boton_diferencia_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: mostrar_operaciones("-"),
    relief="flat"
)
boton_diferencia.place(
    x=1063.0,
    y=24.0,
    width=230.0,
    height=65.0
)

boton_complemento_image = PhotoImage(
    file=relative_to_assets("button_3.png"))
boton_complemento = Button(
    image=boton_complemento_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: mostrar_operaciones("'"),
    relief="flat"
)
boton_complemento.place(
    x=744.0,
    y=24.0,
    width=230.0,
    height=65.0
)

boton_interseccion_image = PhotoImage(
    file=relative_to_assets("button_4.png"))
boton_interseccion = Button(
    image=boton_interseccion_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: mostrar_operaciones("∩"),
    relief="flat"
)
boton_interseccion.place(
    x=448.0,
    y=24.0,
    width=230.0,
    height=65.0
)

boton_union_image = PhotoImage(
    file=relative_to_assets("button_5.png"))
boton_union = Button(
    image=boton_union_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: mostrar_operaciones("u"),
    relief="flat"
)
boton_union.place(
    x=129.0,
    y=24.0,
    width=230.0,
    height=65.0
)

boton_resultados_image = PhotoImage(
    file=relative_to_assets("button_6.png"))
boton_resultados = Button(
    image=boton_resultados_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: mostrar_resultados(canvas.itemcget(texto_conjuntos, 'text'), lista_conjuntos),
    relief="flat"
)
boton_resultados.place(
    x=514.0,
    y=941.0,
    width=411.0,
    height=65.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    710.0,
    855.0,
    image=image_image_1
)

canvas.create_text(
    578.0,
    773.0,
    anchor="nw",
    text="Operación de conjuntos",
    fill="#121C17",
    font=("Inter", 28 * -1)
)

boton_conjuntoD_image = PhotoImage(
    file=relative_to_assets("button_7.png"))
boton_conjuntoD = Button(
    image=boton_conjuntoD_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: mostrar_conjunto("D", entry_subconjuntoD.get()),
    relief="flat"
)
boton_conjuntoD.place(
    x=798.0,
    y=656.0,
    width=230.0,
    height=65.0
)

entry_subconjuntoD_image = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_subconjuntoD_bg = canvas.create_image(
    1089.0,
    610.0,
    image=entry_subconjuntoD_image
)
entry_subconjuntoD = Entry(
    bd=0,
    bg="#E1EAE3",
    fg="#000716",
    highlightthickness=0
)
entry_subconjuntoD.place(
    x=818.0,
    y=580.0,
    width=542.0,
    height=58.0
)

canvas.create_text(
    798.0,
    529.0,
    anchor="nw",
    text="Subconjunto D",
    fill="#121C17",
    font=("Inter", 28 * -1)
)

boton_conjuntoC_image = PhotoImage(
    file=relative_to_assets("button_8.png"))
boton_conjuntoC = Button(
    image=boton_conjuntoC_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: mostrar_conjunto("C", entry_subconjuntoC.get()),
    relief="flat"
)
boton_conjuntoC.place(
    x=75.0,
    y=656.0,
    width=230.0,
    height=65.0
)

entry_subconjuntoC_image = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_subconjuntoC_bg = canvas.create_image(
    366.0,
    610.0,
    image=entry_subconjuntoC_image
)
entry_subconjuntoC = Entry(
    bd=0,
    bg="#E1EAE3",
    fg="#000716",
    highlightthickness=0
)
entry_subconjuntoC.place(
    x=95.0,
    y=580.0,
    width=542.0,
    height=58.0
)

canvas.create_text(
    75.0,
    529.0,
    anchor="nw",
    text="Subconjunto C",
    fill="#121C17",
    font=("Inter", 28 * -1)
)

boton_conjuntoB_image = PhotoImage(
    file=relative_to_assets("button_9.png"))
boton_conjuntoB = Button(
    image=boton_conjuntoB_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: mostrar_conjunto("B", entry_subconjuntoB.get()),
    relief="flat"
)
boton_conjuntoB.place(
    x=798.0,
    y=411.0,
    width=230.0,
    height=65.0
)

entry_subconjuntoB_image = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_subconjuntoB_bg = canvas.create_image(
    1089.0,
    365.0,
    image=entry_subconjuntoB_image
)
entry_subconjuntoB = Entry(
    bd=0,
    bg="#E1EAE3",
    fg="#000716",
    highlightthickness=0
)
entry_subconjuntoB.place(
    x=818.0,
    y=335.0,
    width=542.0,
    height=58.0
)

canvas.create_text(
    798.0,
    284.0,
    anchor="nw",
    text="Subconjunto B",
    fill="#121C17",
    font=("Inter", 28 * -1)
)

boton_conjuntoA_image = PhotoImage(
    file=relative_to_assets("button_10.png"))
boton_conjuntoA = Button(
    image=boton_conjuntoA_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: mostrar_conjunto("A", entry_subconjuntoA.get()),
    relief="flat"
)
boton_conjuntoA.place(
    x=75.0,
    y=411.0,
    width=230.0,
    height=65.0
)

entry_subconjuntoA_image = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_subconjuntoA_bg = canvas.create_image(
    366.0,
    365.0,
    image=entry_subconjuntoA_image
)
entry_subconjuntoA = Entry(
    bd=0,
    bg="#E1EAE3",
    fg="#000716",
    highlightthickness=0
)
entry_subconjuntoA.place(
    x=95.0,
    y=335.0,
    width=542.0,
    height=58.0
)

canvas.create_text(
    75.0,
    284.0,
    anchor="nw",
    text="Subconjunto A",
    fill="#121C17",
    font=("Inter", 28 * -1)
)

entry_universal_image = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_universal_bg = canvas.create_image(
    720.0,
    212.0,
    image=entry_universal_image
)
entry_universal = Entry(
    bd=0,
    bg="#E1EAE3",
    fg="#000716",
    highlightthickness=0
)
entry_universal.place(
    x=449.0,
    y=182.0,
    width=542.0,
    height=58.0
)


canvas.create_text(
    593.0,
    131.0,
    anchor="nw",
    text="Conjunto Universal\n",
    fill="#121C17",
    font=("Inter", 28 * -1)
)

texto_conjuntos = canvas.create_text(
    441.0,
    827.0,
    anchor="nw",
    text="Conjunto Formado",
    fill="#FFFFFF",
    font=("Inter", 28 * -1)
)
boton_parentesis_izq_image  = PhotoImage(
    file=relative_to_assets("button_11.png"))
boton_parentesis_izq = Button(
    image=boton_parentesis_izq_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: mostrar_operaciones("("),
    relief="flat"
)
boton_parentesis_izq.place(
    x=113.0,
    y=822.0,
    width=63.0,
    height=65.0
)

boton_parentesis_der_image = PhotoImage(
    file=relative_to_assets("button_12.png"))
boton_parentesis_der = Button(
    image=boton_parentesis_der_image,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: mostrar_operaciones(")"),
    relief="flat"
)
boton_parentesis_der.place(
    x=266.0,
    y=823.0,
    width=63.0,
    height=65.0
)

# Configurar la fuente del Entry
entry_subconjuntoD.config(font=("Roboto", 20))
entry_subconjuntoC.config(font=("Roboto", 20))
entry_subconjuntoB.config(font=("Roboto", 20))
entry_subconjuntoA.config(font=("Roboto", 20))
entry_universal.config(font=("Roboto", 20))

# Clases
class Conjunto:
    letra = str()
    def __init__(self, letra= str(), lista=None):
        if lista is None:
            lista = []
        self.conjunto = set(lista)
        self.letra = letra
        
    @property
    def Letra(self):
        return self.letra

    @Letra.setter
    def Letra(self, letra):
        self.letra = letra

# Variables

lista_conjuntos = []
texto_operacion = str()
# conjunto_universal = Conjunto("U")
# conjunto_A = Conjunto("A")
# conjunto_B = Conjunto("B")
# conjunto_C = Conjunto("C")
# conjunto_D = Conjunto("D")

# Funciones

def mostrar_conjunto(letra, entry_text):
    global texto_operacion
    global lista_conjuntos
    
    objeto = Conjunto(letra, entry_text.split(","))
    lista_conjuntos.append(objeto)
    
    texto_operacion += letra + " "
    canvas.itemconfig(tagOrId=texto_conjuntos, text=f"{texto_operacion}")
    contenido = canvas.itemcget(texto_conjuntos, 'text')
    print(contenido)
    
def mostrar_operaciones(letra):
    global texto_operacion
    
    texto_operacion += letra + " "
    canvas.itemconfig(tagOrId=texto_conjuntos, text=f"{texto_operacion}")
    
def quitar_texto():
    global texto_operacion
    
    operadores = ["A","B","C","D","u","∩","'","-","(",")"]
    conjuntos = ["A","B","C","D"]
    
    for operador in reversed(texto_operacion):
        if operador in operadores:
            texto_operacion = texto_operacion.replace(operador, "", 1)
            try:
                texto_operacion = texto_operacion.replace(" ", "", 1)
            except:
                pass
            if operador in conjuntos:
                lista_conjuntos.pop
            break
    
    canvas.itemconfig(tagOrId=texto_conjuntos, text=f"{texto_operacion}")

def mostrar_resultados(texto, lista_conjuntos):
    operadores = {"u", "∩", "'", "-"}

    conjunto_actual = set()
    operacion_actual = 'u'  # Operación predeterminada (unión)
    conjunto_temporal = []
    valor_bandera = True
    
    contador = 0
    
    print(len(lista_conjuntos))

    for char in texto:
        if char.isalpha() and char not in operadores:  # Si es una letra, la consideramos como un conjunto
            conjunto_temporal.append(lista_conjuntos[contador].conjunto)
            contador += 1
            print(contador)
        elif char in operadores:  # Si es un operador, cambiamos la operación actual
            operacion_actual = char
        elif char == '(':  # Si es un paréntesis de apertura, reiniciamos el conjunto temporal
            conjunto_temporal = []
        elif char == ')':  # Si es un paréntesis de cierre, realizamos la operación y actualizamos el conjunto actual
            conjunto_actual = realizar_operacion(conjunto_temporal, operacion_actual)
            conjunto_temporal.append(list(conjunto_actual))
            print("l")

    resultado_ordenado = sorted(conjunto_actual)
    # Al final, se puede imprimir o devolver el conjunto final
    print(f"Resultado final: {resultado_ordenado}")
    
    contador = 0
    
    
def realizar_operacion(lista_de_conjuntos, operacion_actual):
    global lista_universal 
    
    lista_universal = entry_universal.get().split(",")
    conjunto_retornar = []
    
    if(operacion_actual == "u"):
        conjunto_retornar = set(lista_de_conjuntos[-1]) | set(list(lista_de_conjuntos[-2]))
        return conjunto_retornar
    
    elif(operacion_actual == "∩"):
        conjunto_retornar = set(lista_de_conjuntos[-1]) & set(lista_de_conjuntos[-2])
        return conjunto_retornar
    
    elif(operacion_actual == "'"):
        conjunto_retornar = set(lista_universal) - set(lista_de_conjuntos[-1])
        return conjunto_retornar
    
    elif(operacion_actual == "-"):
        conjunto_retornar = set(lista_de_conjuntos[-1]) - set(lista_de_conjuntos[-2])
        return conjunto_retornar
    
window.resizable(False, False)
window.mainloop()
