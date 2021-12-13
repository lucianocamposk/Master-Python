"""
Modulos: Son funcionalidades ya hechas para reuilizar.

En python hay muchos modulos, que los puedes consultar aqui:
https://docs.python.org/3/library/math.html#module-math

Podemos conseguir modulos que ya vienen en el lenguaje,
modulos en internet y tambien podemos crear ntros modulos
"""

#Importar modulo propio

# import mimodulo
# from mimodulo import holaMundo
from mimodulo import *

#print(mimodulo.holaMundo('Luciano Kriegl'))
#print(mimodulo.calculadora(3,5,True))

print(holaMundo("Luciano Campos"))
print(calculadora(3,5,True))

# Modulo Fecha
import datetime

print(datetime.date.today())

fecha_completa= datetime.datetime.now()

print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada= fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")
print("Mi fecha personalizada ", fecha_personalizada)

print(datetime.datetime.now().timestamp())


# Modulo matematicas
import math
print("Raiz cuadrada de 10", math.sqrt(10))

print("EL numero pi: " , float( math.pi))

print("Redondear: ", math.ceil(6.66798))
print("Redondear: ", math.floor(6.66798))

# Modulo random
import random

print("Numero aleatorio entre 15 y 67: ", random.randint(15,67))