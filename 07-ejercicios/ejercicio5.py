"""
Ejercicio  5. Hacer un programa que muestre todos
los numeros entre dos numeros que diga el usuario
"""

n1= int(input("introduce primer numero: "))
n2= int(input("introduce segundo numero: "))

if n1 < n2:
    for i in range(n1+1,n2):
        print(i)
else: print("no es correcto")