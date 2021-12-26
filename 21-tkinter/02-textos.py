from tkinter import *

ventana = Tk()
ventana.geometry("700x500")


texto = Label(ventana, text="Bienvenido a mi programa")

texto.config(
            fg="white",
            bg="#000000",
            padx=520,
            pady=20,
            font=("Consolas", 30)
)

texto.pack()


texto = Label(ventana, text="Soy Luciano Campos Kriegl")
texto.config(
    height=3,
    bg="orange",
    font=("Arial",18),
    padx=10,
    pady=30,
    cursor="spider"

)
texto.pack(anchor=SE)

def pruebas(nombre,apellido,pais):
    return f"Hola {nombre} {apellido}, veo que eres de {pais}"

texto = Label(ventana, text=pruebas(nombre="Luciano",apellido="Campos Kriegl", pais="Argentina"))

texto.config(
    height=3,
    bg="green",
    font=("Arial",18),
    padx=10,
    pady=30,
    cursor="spider"

)
texto.pack(anchor=NW)

ventana.mainloop()