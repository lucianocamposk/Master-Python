"""
Ejercicio 6. mostrar todas las tablas de multiplicar
del 1 al 10 mostrando el titulo de la tabla y luego 
las multiplicaciones del 1 al 10
"""

for i in range (1,11):
    print(f"tabla del {i}")
    for a in range(11):
        print(f"{i} X {a} = {i*a} " )