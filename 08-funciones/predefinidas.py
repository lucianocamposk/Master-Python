nombre ="Luciano Kriegl"

## FUNCIONES GENERALES ##

print(type(nombre))

# DETECTAR EL TIPADO

comprobar = isinstance(nombre, str)
if comprobar:
    print("esa variable es un string")
else:
    print("no es una cadena")

if not isinstance(nombre,float):
    print("la variable no es un numero con decimales")

# LIMPIAR ESPACIOS

frase= "  mi   contenido    "
print(frase)
print(frase.strip())

# ELIMINAR VARIABLES

year = 2022
print(year)
del year
#print (year) ya no anda

#comproobar variable vacia

texto=  " ff     "

if len(texto) <= 0:
    print("la variable esta vacia")
else:
    print("la variable tiene contenido:", len(texto))

# ENCONTRAR CARACTERES

frase= "la vida es beia"
print(frase.find("vida"))

# Reemplazas palabras en un string

nueva_frase = frase.replace("vida","moto")
print(nueva_frase)

# MAYUSCULAS Y MINUSCULAS

print(nombre)
print(nombre.lower())
print(nombre.upper())