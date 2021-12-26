from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.title('Ejercicio completo con tkinter | Luciano Campos Kriegl')
ventana.geometry('340x215')
ventana.config(bd=25)


def cFloat(numero):
    try:
        result = float(numero)
    except:
        result = 0
        messagebox.showerror('Error', 'Introduce bien el numero')
    return result
    
def sumar():
    resultado.set(cFloat(numero1.get()) + cFloat(numero2.get()))
    mostrarResultado()
def restar():
    resultado.set(cFloat(numero1.get()) - cFloat(numero2.get()))
    mostrarResultado()
def multiplicar():
    resultado.set(cFloat(numero1.get()) * cFloat(numero2.get()))
    mostrarResultado()
def dividir():
    resultado.set(cFloat(numero1.get()) / cFloat(numero2.get  ()))
    mostrarResultado()

def mostrarResultado():
    messagebox.showinfo('Resultado', f'El resultado es {resultado.get()}')
    numero1.set('')
    numero2.set('')
    
    


numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()

marco = Frame(ventana, width=340, height=215)
marco.config(
    padx=15,
    pady=15,
    bd=5,
    relief=SOLID
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)
Label(marco, text='Primer numero: ').pack()
Entry(marco, textvariable=numero1, justify='center').pack()


Label(marco, text='Segundo numero: ').pack()
Entry(marco, textvariable=numero2, justify='center').pack()

Label(marco,text='')
Button(marco, text='Sumar', command=sumar).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text='Restar', command=restar).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text='Multiplicar', command=multiplicar).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text='Dividir', command=dividir).pack(side=LEFT, fill=X, expand=YES)

ventana.mainloop()