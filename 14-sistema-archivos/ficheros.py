from io import open
import pathlib
import shutil

# Abrir archivo
ruta= str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo = open(ruta,"a+")

# Escribir
archivo.write("***** soy un texto metido desde python ******\n")

# Cerrar archivo
archivo.close()

# Abrir archivo
ruta=str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo_lectura = open(ruta, "r")

# Leer contenido
#contenido= archivo_lectura.read()
#print(contenido)

# Leer contenido y mostrar en listo
lista = archivo_lectura.readlines()
archivo_lectura.close()

for frase in lista:
    #lista_frase = frase.split()
    #print(lista_frase)
    print('- ' +frase.center(100))


# Copiar
"""
ruta_original=str(pathlib.Path().absolute()) + "/fichero_texto.txt"
ruta_nueva=str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
ruta_alternativa=str(pathlib.Path().absolute()) + "/../07-ejercicios/fichero_copiado77.txt"

shutil.copyfile(ruta_original, ruta_nueva)
"""
# Mover
"""
ruta_original=str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
ruta_nueva=str(pathlib.Path().absolute()) + "/fichero_copiado_Nuevo.txt"

shutil.move(ruta_original,ruta_nueva)
"""

# Eliminar
import os
"""
ruta_nueva=str(pathlib.Path().absolute()) + "/fichero_copiado_Nuevo.txt"

os.remove(ruta_nueva)
"""
# Compromar si existe
import os.path

#print(os.path.abspath("./"))

ruta_comprobar =  os.path.abspath("./") + "fichero_texto.txt"
ruta_comprobar= "./fichero_texto.txt"

if os.path.isfile(os.path.abspath("./") + "/fichero_texto.txt"):
    print('el archivo existe')
else:
    print('el archivo no existe')
