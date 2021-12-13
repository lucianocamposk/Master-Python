"""
Ejercicio 9. Hacer un programa que pida numero al usuario
indefinidamente hasta meter el 111
"""
cont = 1
    while cont <100:
        numero = int(input("introduce un numero: "))

        if numero==111:
            break
        else: 
               print(f"Has introducido el: {numero}")