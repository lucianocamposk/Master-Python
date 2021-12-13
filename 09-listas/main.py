"""
LISTAS (arrays)
son colecciones o conjuntos de datos/valores, bajo un
unico nombre.
para acceder a esos valores podemos usar un indicador numerico
"""

pelicula ="Batman"

#DEFINIR LISTA

peliculas=["Batman", "Spiderman", "El señor de los anillos"]
cantantes=list(('2pac','drake', 'jennifer lopez'))
years = list(range(2020,2050))
variada= ["Luciano", 30, 4.4, True, "texto"]
"""
print(peliculas)
print(cantantes)
print(years)
print(variada)
"""

# INDICES

peliculas[1]="Gran torino"

print(peliculas[1])
print(peliculas[-2])
print(cantantes[0:2])
print(cantantes[1:])

# AñADIR ELEMENTO A LA LISTA

cantantes.append("Kase o")
cantantes.append("el duki")
print(cantantes)

# RECORRER LISTA
"""
nueva_pelicula=""
while nueva_pelicula!="parar":
    nueva_pelicula= input("introduce nueva pelicula: ")

    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)

print("\n******LISTADO DE PELICULAS******")

for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)}{pelicula}")
"""

# LISTAS MULDIMENSIONALES

contactos = [

    [
        'Antonio',
        'antonio@antonio.com'

    ],
    [
        'Luis',
        'luils@luis.com'
    ],

    [
        'salvador',
        'salvador@salvador.com'
    ]

]

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento)==0:
            print("Nombre: " + elemento)
        else:
            print("Email: " + elemento)
    print("\n")
