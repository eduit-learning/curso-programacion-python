# Crea un conjunto con una serie de elementos entre llaves
# Los elementos repetidos se eliminan
c = {1, 3, 2, 9, 3, 1}
print(c)

# Crea un conjunto a partir de un string
# Los caracteres repetidos se eliminan
a = set('Hola Pythonista')
print(a)

# Crea un conjunto a partir de una lista
# Los elementos repetidos de la lista se eliminan
unicos = set([3, 5, 6, 1, 5])
print(unicos)

################################################################################33 - frozenset
f = frozenset([3, 5, 6, 1, 5])
print(f)
frozenset({1, 3, 5, 6})

################################################################################33 - Cómo acceder
mi_conjunto = {1, 3, 2, 9, 3, 1}
for e in mi_conjunto:
    print(e)

################################################################################33 - Añadir elementos
mi_conjunto = {1, 3, 2, 9, 3, 1}
print(mi_conjunto)

# Añade el elemento 7 al conjunto
mi_conjunto.add(7)
print(mi_conjunto)

# Añade los elementos 5, 3, 4 y 6 al conjunto
# Los elementos repetidos no se añaden al conjunto
mi_conjunto.update([5, 3, 4, 6])
print(mi_conjunto)

################################################################################33 - Eliminar elementos
mi_conjunto = {1, 3, 2, 9, 3, 1, 6, 4, 5}
print(mi_conjunto)

# Elimina el elemento 1 con remove()
mi_conjunto.remove(1)
print(mi_conjunto)

# Elimina el elemento 4 con discard()
mi_conjunto.discard(4)
print(mi_conjunto)

# Trata de eliminar el elemento 7 (no existe) con remove()
# Lanza la excepción KeyError
print(mi_conjunto.remove(7))#Error

# Trata de eliminar el elemento 7 (no existe) con discard()
# No hace nada
mi_conjunto.discard(7)
print(mi_conjunto)

# Obtiene y elimina un elemento aleatorio con pop()
print(mi_conjunto.pop())
print(mi_conjunto)

# Elimina todos los elementos del conjunto
mi_conjunto.clear()
print(mi_conjunto)

mi_conjunto = set([1, 2, 5, 3, 1, 5])
len(mi_conjunto)

mi_conjunto = set([1, 2, 5, 3, 1, 5])
print(1 in mi_conjunto)
print(6 in mi_conjunto)
print(2 not in mi_conjunto)

################################################################################## - Operaciones de conjuntos
#Unión
a = {1, 2, 3, 4}
b = {2, 4, 6, 8}
print(a | b)

#Intersección
a = {1, 2, 3, 4}
b = {2, 4, 6, 8}
print(a & b)

#Diferencia
a = {1, 2, 3, 4}
b = {2, 4, 6, 8}
print(a - b)

#Diferencia simétrica
a = {1, 2, 3, 4}
b = {2, 4, 6, 8}
print(a ^ b)

#Inclusión
a = {1, 2}
b = {1, 2, 3, 4}
print(a <= b)
print(a >= b)
print(b >= a)

a = {1, 2}
b = {1, 2}
print(a < b)  # Ojo al operador < sin el =
print(a <= b)

#Conjuntos disjuntos
a = {1, 2}
b = {1, 2, 3, 4}
print(a.isdisjoint(b))

a = {1, 2}
b = {3, 4}
print(a.isdisjoint(b))

#Igualdad
a = {1, 2}
b = {1, 2}
print(id(a))
print(id(b))
print(a == b)