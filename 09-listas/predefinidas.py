cantantes = ['2pac', 'Drake', 'bad bunny', ' julio iglesias']
numeros= [1, 2, 5, 8, 3, 4 ]

# ORDENAR
print(numeros)
numeros.sort()
print(numeros)

# AÑADIR ELEMENTOS
cantantes.append("Natos y waor")
cantantes.insert(1,"David Bisbal")

print(cantantes)

# Eliminar elementos
cantantes.pop(1)
cantantes.remove("bad bunny")
print(cantantes)

# DAR LA VUELTA
print(numeros)
numeros.reverse()
print(numeros)

# Buscar dentro de una lista
print('Drake' in cantantes)

# CONTAR ELEMENTOS
print(len(cantantes))

# CUANTAS VECES APARECE UN ELEMENTO
numeros.append(8)
print(numeros.count(8))

# CONSEGUIR INDICE
print(cantantes.index("Drake"))

# UNIR LISTAS
cantantes.extend(numeros)
print(cantantes)