numeros = [1,2,3,4]
print(numeros)

########################################################
datos = [4, "Una cadena", -15, 3.14, "Otra cadena"]
print(datos[0])
print(datos[-3])
#Esto es un slicing
print("Acá*********************************************************************************************************")
print(datos[-4:-1])

########################################################
print(numeros + [5,6,7,8])

########################################################
pares = [0,2,4,5,8,10]
print(pares)
pares[3] = 6
print(pares)
pares.append(12)
pares.append(7*2)
print(pares)

#########################################################

letras = ['a','b','c','d','e','f']
print(letras[:3])
###

letras[:3] = ['A','B','C']# esto es equivalente a: letras[0] = 'A', letras[1] = 'B', letras[2] = 'C'. Si agrego una letrá más que el rango especificado en la izquierda
#éste se agrega a la lista. Si pongo menos elementos que los especificados en la lista se eliminan lo que no empaten.
print(letras)
###

letras[:3] = []#Otra forma de quitar elementos es con el método remove. letras.remove(elemento a elimininar). El inconveniente de este método es que debes saber lo que quieres eliminar
print(letras)

#########################################################
print(len(letras))
print(len(pares))

#########################################################

a = [1,2,3]
b = [4,5,6,10]
c = [7,8,9]
d = ['a', 'b', 'c', 'd', 'e']
r = [a,b,c,d]
s = [r, a]
print(r)
print(s)

print(r[0])       # Primera sublista
print(r[-1])      # Última sublista

print(r[0][0])    # Primera sublista, y de ella, primer ítem
print(r[1][1])    # Segunda sublista, y de ella, segundo ítem
print(r[2][2])    # Tercera sublista, y de ella, tercer ítem
print(r[-1][-1])  # Última sublista, y de ella, último ítem