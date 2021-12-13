"""
SET es un tipo de dato, para tener una coleccion de valores,
pero no tiene ni indice ni orden

"""

personas ={
    "victor",
    "luciano",
    "francisco"
}

personas.add("Paco")
personas.remove("francisco")

print(type(personas))
print(personas)