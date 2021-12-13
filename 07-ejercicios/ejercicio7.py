"""
Ejercicio 7. Hacer un programa que muestre todos los numeros impares
entre dos numero que decida el usuario
"""

n1= int(input("Introduce primer numero: "))

n2= int(input("Introduce segundo numero: "))

if n1<n2:
    for i in range (n1,n2):
        if i%2==1:
            print(i)