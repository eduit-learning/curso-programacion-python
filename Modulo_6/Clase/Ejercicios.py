#Escribir un programa que permita gestionar la base de datos de clientes de una empresa.
#Los clientes se guardarán en en la base de datos (SQLEXPRESS o SQLITE) en el que la clave de cada cliente será su CURP(Puede ser in Id identity),
#y donde cada fila tendrá los datos del cliente (nombre, dirección, teléfono, correo, preferente),
# donde "preferente" tendrá el valor True si se trata de un cliente preferente.
# El programa debe preguntar al usuario por una opción del siguiente menú:
# (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes,
# (5) Listar clientes preferentes, (6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:
#1. Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
#2. Preguntar por el CURP del cliente y eliminar sus datos de la base de datos.
#3. Preguntar por el CURP del cliente y mostrar sus datos.
#4. Mostrar lista de todos los clientes de la base datos con su CURP y nombre.
#5. Mostrar la lista de clientes preferentes de la base de datos con su CURP y nombre.
#6. Terminar el programa.