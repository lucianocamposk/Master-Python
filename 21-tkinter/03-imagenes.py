from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()
ventana.geometry("1151x768")

Label(ventana, text=('Hola soy Luciano!!')).pack(anchor=W)

imagen = Image.open('./21-tkinter/imagenes/lobo_negro.jpg')
render = ImageTk.PhotoImage(imagen)

Label(ventana, image=render).pack()

ventana.mainloop()
