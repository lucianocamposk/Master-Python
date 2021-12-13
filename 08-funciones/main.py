"""
FUNCIONES:
una funcion es un conjunto de instrucciones agrupadas bajo
un nombre concreto que pueden reutilizarse invocando a
la funcion tantas veces como sea neecesaria

def nombreDeMiFuncion(parametros):
    #BLOQUE / CAMPO DE INSTRUCCIONES

nombreDeMifuncion(mi_parametro)

"""
"""
#EJEMPLO 1

print("####### EJEMPLO 1 #######")

# definir funcion
def muestraNombre():
    print("victor")
    print("vicotria")
    print("ernesto")
    print("luciano")
    print("joaquin")
    print("juana")

# invocar funcion
muestraNombre()



#EJEMPLO 2
print("####### EJEMPLO 2 #######")
def mostrarTuNombre(nombre,edad):
    print(f"Tu nombre es: {nombre}")
    
    if edad>=18:
        print("Y eres mayor de edad")

nombre= input("introduce tu nombre ")
edad= int(input("introduce tu edad "))

mostrarTuNombre(nombre,edad)

#Ejemplo 3

def tabla(numero):
    print(f"tabla de multiplicar del numero: {numero}")

    for contador in range(11):
        operacion = numero*contador
        print(f"{numero} x {contador} = {operacion}")
    
    print("\n")


tabla(3)
tabla(7)
tabla(12)

#ejemplo 3.1
for numero_tabla in range (1,11):
    tabla(numero_tabla)

"""

#ejemplo 4

#parametros opcionales

def getEmpleado(nombre, dni=None):
    print("empleado")
    print(f"nombre: {nombre}")
    if dni != None:  
         print(f"dni: {dni}")

getEmpleado("luciano")

#ejemplo 5:  return o devolver datos

def saludame (nombre):
    saludo = f"hola, saludos {nombre}"

    return saludo

print(saludame("Luciano campos"))

def calculadora(numero1, numero2, basicas = False):
    suma= numero1 + numero2
    resta= numero1 - numero2
    multi= numero1 * numero2
    division= numero1 / numero2

    cadena = ""
    if basicas!= False:
    
        cadena+= "Suma: " + str(suma)
        cadena+= "\n"
        cadena+= "resta: " + str(resta)
        cadena+= "\n"
    else:
        cadena+= "multiplicacion: " + str(multi)
        cadena+= "\n"
        cadena+= "division: " + str(division)

    return cadena

print(calculadora(56,5,True))

#Ejemplo 7

print("\n######## 7 #######")

def getNombre(nombre):
    texto= f"El nombre es: {nombre}"
    return texto

def getApellidos(apellidos):
    texto= f"los apellidos son: {apellidos}"
    return texto

def devuelveTodo(nombre, apellidos):
    texto= getNombre(nombre) + "\n" + getApellidos(apellidos)
    return texto

print(devuelveTodo("luciano","kriegl"))

#Ejemplo 8: Funciones lambda
print("\n######## 8 #######")

dime_el_year = lambda year: f"El año es {year}"

print(dime_el_year(2034))
