numeros = 1, 2, 3, 4, 5
elementos = 3, 'a', 8, 7.2, 'hola'
tup = 1, ['a', 'e', 'i', 'o', 'u'], 8.9, 'hola'

# Aquí, a, b y c no son una tupla, sino tres argumentos con
# los que se llama a la función "una_funcion"
una_funcion(a, b, c)

# Aquí, a, b y c son tres elementos de una tupla. Esta tupla,
# es el único argumento con el que se invoca a la 
# función "una_funcion"
una_funcion((a, b, c))

#######################################################################33 - Cómo acceder a los elementos de una tupla
tupla = ('a', 'b', 'd')
print(tupla[0])  # Primer elemento de la tupla. Índice 0
print(tupla[1])  # Segundo elemento de la tupla. Índice 1

tupla = 1, 2, 3  # Los índices válidos son 0, 1 y 2
print(tupla[8])#error

print(tupla[1.0])

#######################################################################33 - Cómo acceder a los elementos de una tupla con índice negativo
bebidas = ('agua', 'café', 'batido', 'sorbete')
print(bebidas[-1])
print(bebidas[-3])

#######################################################################33 - Cómo acceder a un subconjunto
vocales = 'a', 'e', 'i', 'o', 'u'
print(vocales[2:3])  # Elementos desde el índice 2 hasta el índice 3-1
print(vocales[2:4])  # Elementos desde el 2 hasta el índice 4-1
print(vocales[:])  # Todos los elementos
print(vocales[1:])  # Elementos desde el índice 1
print(vocales[:3])  # Elementos hasta el índice 3-1

pares = 2, 4, 6, 8, 10, 12, 14
print(pares[::2])  # Acceso a los elementos de 2 en 2
print(pares[1:5:2])  # Elementos del índice 1 al 4 de 2 en 2
print(pares[1:6:3])  # Elementos del índice 1 al 5 de 3 en 3

#A esto se le conoce como "unpacking"
bebidas = 'agua', 'café', 'batido'
a, b, c = bebidas
print(a)
print(b)
print(c)

#######################################################################33 - Cómo acceder con for
colores = 'azul', 'blanco', 'negro'
for color in colores:
    print(color)

#######################################################################33 - Modificar
tupla = (1, ['a', 'b'], 'hola', 8.2)
tupla[1].append('c')  # tupla[1] hace referencia a la lista
print(tupla)

vocales = ('a', 'e', 'i', 'o', 'u')
print(len(vocales))

colores = 'azul', 'blanco', 'negro'
if 'azul' in colores:
    print('Sí')

if 'verde' not in colores:
    print('No')