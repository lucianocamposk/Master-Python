"""
Ejercicio 1. Hacer un programa que tenga una lista
de 8 numeros enteros y haga lo siguiente:
-Recorrer la lista y mostrarla
-hacer funcion que recorrar listas de numeros y devuelva un string para mostrar
-Ordenarla y mostrarla
-Mostrar su longitud
-Buscar algun elemento( que el usuario pida por teclado)
"""


# Crear la lista
numeros = [13,52,12,52,12,56,54]

# Crear funcion que recorra lista y devuelva string

def mostrarLista(lista):
    resultado=""

    for elemento in lista:
        resultado+="Elemento: " + str(elemento)
        resultado+="\n"
    
    return resultado

# Recorrer y mostrar
print("########## RECORRER Y MOSTRAR #######")
"""
for numero in numeros:
    print(numero)
"""
print(mostrarLista(numeros))
print(mostrarLista(["victor","juan","cecilia"]))

# Ordenar y mostrar

print("###### ORDENAR Y MOSTRAR ######")
numeros.sort()
print(mostrarLista(numeros))

# Mostrar su longitud
print("###### CONTAR ELEMENTOS ######")

print(len(numeros))

# Busqueda en la lista

busqueda= int(input("introduce el numero: "))

comprobar= isinstance(busqueda, int)
while not comprobar or busqueda <=0:    
    busqueda= int(input("introduce el numero: "))
else:
     print(f"Has introducido el {busqueda}")



print(f"##### Buscar en la lista el numero {busqueda} #####")

search= numeros.index(busqueda)
print(f"El numero buscado existe en la lista, es el indice: {search}")


