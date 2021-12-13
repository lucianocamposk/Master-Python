"""
Variables locales: se definen dentro e la funcion y no
se puede usar fuera de ella, solo estan disponibles dentro
a no ser que hagamos un return

variables globales: son las que se declaran fuera de una funcion
y estan disopnibles dentro y fuera de ellas

"""

#Variable global
frase="Ni los genios son tan genios, ni los mediocres tan mediocres"

print(frase)

def holaMundo():
    frase="Hola mundo!!"
    print("Dentro de la funcion: ")
    print(frase)

    year= 2021
    print(year)

    global website
    website="victorroblesweb.es"
    print("DENTRO: ", website)

    return "Dato devuelto " +str(year)

print(holaMundo())
print("FUERA: ", website)