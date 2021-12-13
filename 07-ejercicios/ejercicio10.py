"""
EJercicio 10. El programa tiene que pedir la nota de 15 alumnos 
y sacar por pantalla cuantos han aprobado y cuantos han suspendido

"""

i=1
aprobados=0
desaprobados=0

alumnos= int(input("Introduce cantidad de alumnos: "))


while i <= alumnos:
    nota=int(input(f"¿Que nota quiere ponerle al \"alumno {i}\"?: "))

    if nota>=6:
        aprobados+=1
    else:
        desaprobados+=1
    i+=1

print(f"Alumnos aprobados: {aprobados} \nalumnos desaprobados: {desaprobados}")



