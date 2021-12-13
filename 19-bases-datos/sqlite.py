# importar modulo
import sqlite3

# conexion

conexion = sqlite3.connect('./19-bases-datos/pruebas.db')

# crear cursor
cursor = conexion.cursor()

# crear tabla
cursor.execute("""CREATE TABLE IF NOT EXISTS productos(
id INTEGER PRIMARY KEY AUTOINCREMENT,
titulo varchar(255), 
descripcion text, 
precio int (255)
)""")

# guardar cambios
conexion.commit()

"""
# insertar datos
cursor.execute("INSERT INTO productos VALUES (null, 'Primer producto', 'descripcion de mi producto', 550)")
conexion.commit()
"""

# Borrar registros
cursor.execute("DELETE FROM productos")
conexion.commit()
#insertar muchos registros de golpe
productos = [
    ("ordenador portatil", "Buen pc", 700),
    ("telefono movil", "Buen telefono", 140),
    ("placa base", "Buena placa", 80),
    ("tablet 15", "Buen tablet", 300),

]
cursor.executemany("INSERT INTO productos VALUES(null,?,?,?)", productos)
conexion.commit()

# Update
cursor.execute("UPDATE productos SET precio =678 WHERE precio = 80")

# listar datos
cursor.execute("SELECT * FROM productos WHERE precio >= 300;")

productos = cursor.fetchall()

for producto in productos:
    print("ID:", producto[0])    
    print("Titulo:", producto[1])
    print("Descripcion:", producto[2])
    print("precio:", producto[3])
    print("\n")

cursor.execute("SELECT titulo FROM productos;")
producto= cursor.fetchone()
print(producto)
# cerrar conexion
conexion.close