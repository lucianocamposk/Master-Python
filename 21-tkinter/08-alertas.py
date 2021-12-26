from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.config(bd=70)

def sacarAlerta():
    MessageBox.showerror('Alerta', 'Hola soy Luciano')

Button(ventana,text='Mostrar alerta!!!!', command=sacarAlerta).pack()

def salir(nombre):
    resultado = MessageBox.askquestion('Salir', '¿Desea salir?')
    if resultado == 'yes':
        MessageBox.showinfo('Adios', f'Hasta luego {nombre}')
        ventana.destroy()

Button(ventana, text='Salir', command=lambda: salir('Luciano Campos Kriegl')).pack()

ventana.mainloop()    