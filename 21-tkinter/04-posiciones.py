from tkinter import *

ventana = Tk()
ventana.geometry()


texto = Label(ventana, text="Bienvenido a mi programa")

texto.config(
    height=3,
    bg="purple",
    font=("Arial",18),
    padx=10,
    pady=30,
    cursor="spider"

)
texto.pack(side=TOP, fill=X, expand= YES)

texto = Label(ventana, text="Bienvenido a mi programa")

texto.config(
    height=3,
    bg="pink",
    font=("Arial",18),
    padx=10,
    pady=30,
    cursor="spider"

)
texto.pack(side=LEFT, fill=X, expand= YES)

texto = Label(ventana, text="Bienvenido a mi programa")

texto.config(
    height=3,
    bg="green",
    font=("Arial",18),
    padx=10,
    pady=30,
    cursor="spider"

)
texto.pack(side=LEFT, fill=X, expand= YES)

texto = Label(ventana, text="Bienvenido a mi programa")

texto.config(
    height=3,
    bg="blue",
    font=("Arial",18),
    padx=10,
    pady=30,
    cursor="spider"

)
texto.pack(side=LEFT, fill=X, expand= YES)

ventana.mainloop()