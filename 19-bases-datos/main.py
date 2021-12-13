import mysql.connector

# Conexion
database = mysql.connector.connect(

    host="localhost",
    user="root",
    passwd="",
    database= ""
)

# La conexion ha sido correcta?
#print(database)

cursor = database.cursor(buffered=True)

cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

cursor.execute("SHOW DATABASES")

for db in cursor:
    print(db)

#crear tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10,2) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)"""
)

cursor.execute("SHOW TABLES")

for table in cursor:
    print(table)


#cursor.execute("INSERT INTO vehiculos VALUES(null, 'Opel', 'Astra', 18500)")
database.commit()
coches = [
    ('Seat', 'Ibiza', 5000),
    ('Renault','Clio', 15000),
    ('Citroen', 'Saxo', 2000),
    ('Mercedes', 'Clase C', 35000)
        ]
#cursor.executemany("INSERT INTO vehiculos VALUES(null,%s,%s,%s)",coches)
database.commit()


cursor.execute("SELECT * FROM vehiculos WHERE precio <= 5000 AND marca = 'Seat'")

result = cursor.fetchall()

print( '--- TODOS MIS COCHES --- ')

for coche in result:
    print(coche[1],coche[3])

cursor.execute("SELECT * FROM vehiculos")
coche= cursor.fetchone()
print(coche)
