"""
Crear un programa que tenga:
(hecho)- Ventana
(hecho)- Tamaño fijo
(hecho)- No redimensionable
(hecho)- Un menu (Inicio, Añadir, Informacion, Salir)
(hecho)- Opcion de salir
(hecho)- Diferentes pantallas
- Formulario de añadir productos
- Guardar datos temporalmente
- Mostrar datos listados en la pantalla home
"""
from tkinter import *
from tkinter import font

# Definir ventana
ventana = Tk()
ventana.geometry('400x400')
ventana.title('Proyecto Tkinter - Master en Python')
ventana.resizable(0,0)


def home():
    # Mostrar pantalla
    home_label.config(
        fg='white',
        bg='black',
        font=('Arial', 30),
        padx=170,
        pady=30
    )
    home_label.grid(row=0, column=0)

    # Ocultar otras pantallas
    add_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()

def add():
    # Encabezado
    add_label.config(
        fg='white',
        bg='black',
        font=('Arial', 30),
        padx=70,
        pady=30
    )
    add_label.grid(row=0, column=0, columnspan=10)
    # Campos de formulario
    add_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
    add_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    add_price_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
    add_price_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    add_description_label.grid(row=3, column=0, padx=5, pady=5, sticky=NE)
    add_description_entry.grid(row=3, column=1, sticky=W,padx=5,pady=5)
    add_description_entry.config(
        width=30,
        height=5,
        font=('Consolas',12),
        padx=15,
        pady=15
        )
    add_separator.grid(row=4)
    add_button.grid(row=5,column=1, sticky=E)
    add_button.config(
        bg='green',
        fg='white',
        pady=5,
        padx=10

    )

    # Ocultar otras pantallas
    home_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()

def info():
    info_label.config(
        fg='white',
        bg='black',
        font=('Arial', 30),
        padx=110,
        pady=30
    )
    info_label.grid(row=0, column=0)
    data_label.grid(row=1, column=0)

    # Ocultar otras pantallas
    add_label.grid_remove()
    home_label.grid_remove()

# Definir campos de pantalla (INICIO)
home_label = Label(ventana, text='Inicio')

# Definir campos de pantalla (ADD)
add_label = Label(ventana, text='Añadir producto')

# Variables importantes
name_data = StringVar()
price_data = StringVar()
# Campos del formulario
add_name_label = Label(ventana, text='Nombre: ')
add_name_entry = Entry(ventana, textvariable=name_data)

add_price_label = Label(ventana, text='Precio: ')
add_price_entry = Entry(ventana, textvariable=price_data)

add_description_label = Label(ventana, text='Descripcion: ')
add_description_entry = Text(ventana)

add_separator =Label(ventana, text='')

add_button = Button(ventana, text='Guardar')


# Definir campos de pantalla (INFO)
info_label = Label(ventana, text='Información')
data_label = Label(ventana, text='Creado por Luciano Campos K. - 2022')
# Cargar pantalla de inicio
home()


# Menu superior
menu_superior = Menu(ventana)
menu_superior.add_command(label='Inicio', command=home)
menu_superior.add_command(label='Añadir', command=add)
menu_superior.add_command(label='Información', command=info)
menu_superior.add_command(label='Salir', command=ventana.quit)

#Cargar menu
ventana.config(menu=menu_superior)

# Cargar ventana
ventana.mainloop()