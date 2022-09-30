import os

os.system('cls')

#with open(r'C:\temp\EmailConfig.csv', 'r') as f:
#    contenido = f.read()
#    print(contenido)

#with open(r'C:\temp\EmailConfig.csv', 'r') as f:
#    for linea in f:
#        print(linea)

#f = open(r'C:\temp\EmailConfig.csv', 'r')
#try:
#    for linea in f:
#        print(linea)
#except Exception as ex:
#    print(f"Ocurrió un error al procesar el archivos. {ex}")
#finally:
#    f.close()



###############################Escritura de archivos
#############Modos en los que puedes abrir un archivo
#r	Solo lectura. El fichero solo se puede leer. Es el modo por defecto si no se indica.
#w	Solo escritura. En el fichero solo se puede escribir. Si ya existe el fichero, reemplaza su contenido.
#a	Adición. En el fichero solo se puede escribir. Si ya existe el fichero, todo lo que se escriba se añadirá al final del mismo.
#x	Como ‘w’ pero si existe el fichero lanza una excepción.
#r+	Lectura y escritura. El fichero se puede leer y escribir.

#with open('C:\\temp\\EmailConfig123.csv', 'w') as f:
#    f.write('Hola Mundo\n')

#with open(r'C:\temp\EmailConfig123.csv', 'w') as f:
#    f.write('Este es otro Hola Mundo\n')

#try:
#    with open(r'C:\temp\EmailConfig123.csv', 'x') as f:
#        f.write('Hola Mundo\n')
#except Exception as ex:
#    print(f"Error: {ex}")

#with open(r'C:\temp\EmailConfig123.csv', 'a') as f:
#    f.write('Hola Mundo\n')
#
#with open(r'C:\temp\EmailConfig123.csv', 'r+') as f:
#    f.write('Mundo con r+++++++++++++++++++++++++++++++++++++++++++asd\n')

with open(r'C:\temp\EmailConfig123.csv', 'r+') as f:
    f.read()
    f.write('Hola Mundo con r+\n')