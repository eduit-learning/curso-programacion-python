x = 17
if x < 20:
    print('x es menor que 20')

valores = [1, 3, 4, 8]
if 5 in valores:
    print('está en valores')
    print('fin')

resultado = None
x = 10
y = 2
if y != 0:
    resultado = x / y
else:
    resultado = f'No se puede dividir {x} entre {y}'
print(resultado)

x = 28
if x < 0:
    print(f'{x} es menor que 0')
elif x > 0:#else { if(x > 0) {...}} ||| else if(x > 0){...}
    print(f'{x} es mayor que 0')
else:
    print('x es 0')

x = 28
if x < 0:
    print(f'{x} es menor que 0')
else:
    if x > 0:
        print(f'{x} es mayor que 0')
    else:
        print('x es 0')

########################################################################
numero = 0
print('Tabla del 3')
while numero <= 10:
    print(f'{numero * 3}')
    numero += 1
print('Fin')

valores = [5, 1, 9, 2, 7, 4]

encontrado = False
indice = 0
longitud = len(valores)
while not encontrado and indice < longitud: ##"not encontrado" es lo mismo que "encontrado == False"
    valor = valores[indice]
    if valor == 2:
        encontrado = True
    else:
        indice += 1
if encontrado:
    print(f'El número 2 ha sido encontrado en el índice {indice}')
else:
    print('El número 2 no se encuentra en la lista de valores')

valores = [5, 1, 9, 2, 7, 4]

encontrado = False
indice = 0
longitud = len(valores)
while indice < longitud:
    valor = valores[indice]
    if valor == 2:
        encontrado = True
        break
    else:
        indice += 1
if encontrado:
    print(f'El elemento 2 ha sido encontrado en el índice {indice}')
else:
    print('El elemento 2 no se encuentra en la lista de valores')

print("Acá*************************************************")
indice = 0
longitud = len(valores)
while indice < longitud:
    valor = valores[indice]
    if valor == 2:
        print("Se encontró el número 2 y se rompe el ciclo")
        break
    else:
        print(indice)
        #continue
        indice += 1


###############################################################################
nums = [4, 78, 9, 84]
for n in nums:
    print(n)

valores = {'A': 4, 'E': 3, 'I': 1, 'O': 0}
for k in valores:
    print(k)

valores = {'A': 4, 'E': 3, 'I': 1, 'O': 0}
for v in valores.values():
    print(v)

valores = {'A': 4, 'E': 3, 'I': 1, 'O': 0}
for k, v in valores.items():
    print('k=', k, ', v=', v)

for i in range(11):
    print(i)

coleccion = [2, 4, 5, 7, 8, 9, 3, 4]
for e in coleccion:
    if e == 7:
        break
    print(e)

coleccion = [2, 4, 5, 7, 8, 9, 3, 4]
for e in coleccion:
    if e % 2 != 0:
        continue
    print(e)

numeros = [1, 2, 4, 3, 5, 8, 6]

for n in numeros:
    if n == 3:
        break
else:
    print('No se encontró el número 3')
