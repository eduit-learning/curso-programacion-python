#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por
#pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario y <n> es el número de letras que tienen el nombre.
nombre = input("¿Cómo te llamas? ")
print(nombre.upper() + " tiene " + str(len(nombre)) + " letras")

#Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país
# +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de
# teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
tel = input("Introduce un número de teléfono con el formato +xx-xxxxxxxxxx-xx: ")
print('El número de teléfono es ', tel[4:-3])

#Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.
frase = input("Introduce una frase: ")
print(frase[::-1])

#Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla
# la misma frase pero con la vocal introducida en mayúscula.
frase = input("Introduce una frase: ")
vocal = input("Introduce una vocal en minúscula:  ")
print(frase.replace(vocal, vocal.upper()))

#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde
# 1 hasta ese número separados por comas.
print("Acá*************************************************************************************************************")
n = int(input("Introduce un número entero positivo: "))
for i in range(1, n+1, 2):
    print(i, end=", ")

#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese
# número hasta cero separados por comas.
n = int(input("Introduce un número entero positivo: "))
for i in range(n, -1, -1):
    print(i, end=", ")

#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra
# introducida empezando por la última.
word = input("Introduce una palabra: ")
for i in range(len(word)-1, -1, -1):
    print(word[i])

#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces
# que aparece la letra en la frase.
frase = input("Introduce una frase: ")
letra = input("Introduce una letra")
contador = 0
for i in frase:
    if i == letra:
        contador += 1
print("La letra '%s' aparece %2i veces en la frase '%s'." % (letra, contador, frase))

#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
n = int(input("Introduce un número entero positivo mayor que 2: "))
i = 2
while n % i != 0:
    i += 1
if i == n:
    print(str(n) + " es primo")
else:
    print(str(n) + " no es primo")

n = int(input("Introduce un número entero positivo mayor que 2: "))
for i in range(2, n):
    if n % i == 0:
        break
if (i + 1)  == n:
    print(str(n) + " es primo")
else: 
    print(str(n) + " no es primo")

#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir”
# que terminará.
while True:
    frase = input("Introduce algo: ")
    if frase.lower() == "salir":
        break
    print(frase)