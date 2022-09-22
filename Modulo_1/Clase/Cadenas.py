print('Hola Mundo')
print("Hola Mundo")
print('Este texto incluye unas " "')
print("Esta 'palabra' se encuentra escrita entre comillas simples")
print(r"Esta \"palabra\" se encuentra escrita entre comillas dobles")
print('Esta \'palabra\' se encuentra escrita entre comillas simples')
print("Un texto\tuna tabulación")
print("Un texto\n\runa nueva línea")
print("C:\nombre\directorio")
print(r"C:\nombre\directorio")  # r(cadena) => raw (cruda)
print("""Una línea
otra línea
otra línea\tuna tabulación""")

###########################################################################
c = "Esto es una cadena\ncon dos líneas"
print(c)
print(c + c)

s = "Una cadena" " compuesta de dos cadenas"
print(s)

diez_espacios = "a" * 100#Esto es igual a: diez_espacios = "aaaaaaaaaa"
print(diez_espacios + "un texto a diez espacios")

palabra = "Python"
print(palabra[0]) # carácter en la posición 0
print(palabra[3])
print(palabra[-1])

print(palabra[-0]) 
print(palabra[-2])
print(palabra[-6])

palabra = "Python"
print(palabra[0:2])#Esto es un slice

print(palabra[-2:])#Puedes colocar un número mayor incluso fuera de los indices
print(palabra[:2])#Esto es igual a: [0:2]
print(palabra[2:])
print(palabra[:])
print(palabra[:2] + palabra[2:])
#print(palabra[99])
print(palabra[:99])
print(palabra[99:])
print(palabra[0:-10])
print("Acá***************************************")
#palabra[0] = "N"#Las cadenas son inmutables, es decir, no se pueden modificar, siquiere que ahora diga Nython debes asignar
#Toda la palabra a la variable: palabra = "Nython"

##palabra tiene "Python"
palabra = "Nñlkñllñ" + palabra[1:]
print(palabra)

palabra = "Python"
print(len(palabra))