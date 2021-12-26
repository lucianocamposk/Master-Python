from tkinter import *
from tkinter import font

ventana = Tk()
ventana.geometry('700x400')
ventana.title('0-6 formularios con tkinter')

encabezado = Label(text='Formularios con Tkinter')

encabezado.config(
    bg='darkgray',
    fg='white',
    font='Arial, 20',
    pady=10,
    padx=10
)
encabezado.grid(row=0, column=0, columnspan=12, sticky=W)

# Label para el campo 
label = Label(ventana, text='Nombre')
label.grid(row=1, column=0, padx=5, pady=5)

# Campo de texto
campo_texto= Entry()
campo_texto.grid(row=1, column=1, padx=5, pady=5)


# Label para el campo (apellido)
label = Label(ventana, text='Apellido')
label.grid(row=2, column=0, padx=5, pady=5)

# Campo de texto (apellido)
campo_texto= Entry()
campo_texto.grid(row=2, column=1, padx=5, pady=5)
campo_texto.config(justify='right', state='normal')

#Label para el campo (desceipcion)
label = Label(ventana, text='Descripcion')
label.grid(row=3, column=0,sticky=N, padx=5, pady=5)

# Campo de texto GRANDE (Descripción)
campo_grande = Text(ventana)
campo_grande.grid(row=3, column=1)
campo_grande.config(
    width=30,
    height=5,
    font=('Arial',12),
    padx=15,
    pady=15
)

# Boton
Label(ventana).grid(row=4,column=1)

boton = Button(ventana, text='Enviar')
boton.grid(row=5, column=1, sticky=W)
boton.config(padx=10, pady=10, bg='green', fg='white')




ventana.mainloop()

 