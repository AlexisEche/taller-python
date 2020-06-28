import sqlite3

#CASE SENSITIVE
# CREAR BASE DE DATOS -- INSERTAR UNA TABLA -- INSERTAR LISTA DE DATOS -- CONSULTA -- WHERE -- ORDERNAR -- ACTUALIZAR-- BORRAR

#PRIMERO

conexion = sqlite3.connect("nuevaBasedeDatos.db")
cursor = conexion.cursor()



lista_personas = [('Kevin','Lalupu','Rumiche',25),('Maryuri','Sandoval','Bodadilla',20),('Luis','Moscol','Fernandez',18)]


#cursor.executemany("INSERT INTO PERSONAS VALUES (?,?,?,?)",lista_personas)

cursor.execute("INSERT INTO PERSONAS VALUES ('Nilton','Saldarriaga','Santur',21)")


cursor.execute("SELECT * FROM PERSONAS")

personas = cursor.fetchall()

for i in personas:
    print(i)

# SEGUNDO
conexion.commit()  # CONFIRMAMOS ALGUN CAMBIO
conexion.close()   # CERRAMOS LA BASE DE DATOS



'''
cursor.execute("SELECT * FROM PERSONAS ORDER by edad")

personas_ordenadas = cursor.fetchall()

for i in personas_ordenadas:
    print(i)

'''

'''
cursor.execute("SELECT * FROM PERSONAS WHERE edad < 24")

personas_seleccionadas = cursor.fetchall()

for i in personas_seleccionadas:
    print(i)

'''
'''
cursor.execute("DELETE FROM PERSONAS WHERE edad > 21")

personas_eliminadas = cursor.fetchall()

for i in personas_eliminadas:
    print(i)

'''

'''
cursor.execute("UPDATE PERSONAS SET apellido2 = 'Sandoval' WHERE name = 'Luis'")

personas_actualizadas = cursor.fetchall()

for i in personas_actualizadas :
    print(i)

'''

#cursor.executemany("INSERT INTO PERSONAS VALUES (?,?,?,?)",lista_personas)
#cursor.execute("CREATE TABLE PERSONAS(nombre TEXT, apellido1 TEXT, apellido2 TEXT, edad INTEGER)")
#cursor.execute("INSERT INTO PERSONAS VALUES ('Joel ','Crisanto ','Hernandez', 21)")
#cursor.execute("INSERT INTO PERSONAS VALUES ('Nilton ','Saldarriaga ','Santur', 23)")
#cursor.execute("INSERT INTO PERSONAS VALUES ('Alexis ','Eche ','Paiva', 24)")