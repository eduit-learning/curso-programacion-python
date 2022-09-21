numeros = [1,2,3,4]
print(numeros)

########################################################
datos = [4, "Una cadena", -15, 3.14, "Otra cadena"]
print(datos[0])
print(datos[-3])
#Esto es un slicing
print(datos[2:])

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
letras[:3] = ['A','B','C']
print(letras)
###
letras[:3] = []
print(letras)

#########################################################
print(len(letras))
print(len(pares))

#########################################################
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
r = [a,b,c]
print(r)

print(r[0])       # Primera sublista
print(r[-1])      # Última sublista

print(r[0][0])    # Primera sublista, y de ella, primer ítem
print(r[1][1])    # Segunda sublista, y de ella, segundo ítem
print(r[2][2])    # Tercera sublista, y de ella, tercer ítem
print(r[-1][-1])  # Última sublista, y de ella, último ítem