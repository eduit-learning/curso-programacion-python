#Escribir un programa que pregunte al usuario los números ganadores de la lotería nacional,
#los almacene en una lista y los muestre ordenados de menor a mayor.
##awarded = []
##for i in range(6):
##    awarded.append(int(input("Introduce un número ganador: ")))
##awarded.sort()
##print("Los números ganadores son " + str(awarded))


#Escribir un programa que almacene en una lista los números del 1 al 10
#y los muestre por pantalla en orden inverso separados por comas.
##numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
##for i in range(1, 11):
##    print(numbers[-i], end=", ")
##
##numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
##numbers.reverse()
##for number in numbers:
##    print(number, end=", ")

#Escribir un programa que almacene las materias de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
#en una lista, pregunte al usuario la calificación que ha sacado en cada materia y elimine de la lista las materias aprobadas.
#Al final el programa debe mostrar las materias que el usuario tiene que repetir.
##subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
##passed = []
##for subject in subjects:
##    score = float(input("¿Qué nota has sacado en " + subject + "?"))
##    if score >= 5:
##        passed.append(subject)
##for subject in passed:
##    subjects.remove(subject)
##print("Tienes que repetir " + str(subjects))
##
##subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
##for i in range(len(subjects)-1, -1, -1):
##    score = float(input("¿Qué nota has sacado en " + subjects[i] + "?"))
##    if score >= 5:
##        subjects.pop(i)
##print("Tienes que repetir " + str(subjects))

#Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3,
#y muestre por pantalla la lista resultante.
###alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
###for i in range(len(alphabet), 1, -1):
###    if i % 3 == 0:
###        alphabet.pop(i-1)
###print(alphabet)

###########################3333#Resolver de una manera distinta
##alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
##for i in range(1, len(alphabet), 3):
##    print(i)
##    print(alphabet[i-1])
##    alphabet.pop(i-1)
##print(alphabet)

#Escribir un programa que pida al usuario una palabra y muestre si es un palíndromo.
##originalWord = input("Introduce una palabra: ")
##word = list(originalWord.replace(' ', '').lower())
##reversed_word = list(originalWord.replace(' ', '').lower())
##reversed_word.reverse()
##if word == reversed_word:
##    print("Es un palíndromo")
##else:
##    print("No es un palíndromo")

#Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8,
#y muestre por pantalla el menor y el mayor de los precios.
##prices = [50, 75, 46, 22, 80, 65, 8]
##min = max = prices[0]
##for price in prices:
##    if price < min:
##        min = price
##    elif price > max:
##        max = price 
##print("El mínimo es " + str(min)) 
##print("El máximo es " + str(max))

#Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre el producto escalar.
#El resultado es: 5
##a = (1, 2, 3)
##b = (-1, 0, 2)
##product = 0
##for i in range(len(a)):
##    product += a[i]*b[i]
##print("El producto de los vectores" + str(a) + " y " + str(b) + " es " + str(product))

#Escribir un programa que almacene las matrices
#A = 1 2 3    y   B = -1 0
#    4 5 6             0 1
#                      1 1
#en una lista y muestre su producto. Nota: Para representar matrices mediante listas usar listas anidadas,
#representando cada vector fila en una lista. El resultado es (2, 5) (2, 11)
##a = ((1, 2, 3),
##     (4, 5, 6))
##b = ((-1, 0),
##     (0, 1),
##     (1,1))
##result = [[0,0],
##          [0,0]]
##for i in range(len(a)):
##    for j in range(len(b[0])):
##        for k in range(len(b)):
##            result[i][j] += a[i][k] * b[k][j]
##for i in range(len(result)):
##    result[i] = tuple(result[i])
##result = tuple(result)
##for i in range(len(result)):
##    print(result[i])


#Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'},
#pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
###monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
###moneda = input("Introduce una divisa: ")
###print(monedas.get(moneda.title(), "La divisa no está."))
###
###monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
###moneda = input("Introduce una divisa: ")
###if moneda.title() in monedas:
###    print(monedas[moneda.title()])
###else:
###    print("La divisa no está.")

#Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla,
#pregunte al usuario por una fruta, el número de kilos y muestre por pantalla el precio de ese número de kilos de fruta.
#Si la fruta no está en el diccionario debe mostrar un mensaje informandolo.
#Fruta	Precio
#Plátano	1.35
#Manzana	0.80
#Pera	0.85
#Naranja	0.70
###frutas = {'Plátano':1.35, 'Manzana':0.8, 'Pera':0.85, 'Naranja':0.7}
###fruta = input('¿Qué fruta quieres? ').title()
###kg = float(input('¿Cuántos kilos? '))
###if fruta in frutas:
###    print(kg, 'kilos de', fruta, 'valen', frutas[fruta]*kg, '€')
###else: 
###    print("Lo siento, la fruta", fruta, "no está disponible.")

#Escribir un programa que permita gestionar la base de datos de clientes de una empresa.
#Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su CURP,
#y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente),
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
###clientes = {}
###opcion = ''
###while opcion != '6':
###    if opcion == '1':
###        curp = input('Introduce CURP del cliente: ')
###        nombre = input('Introduce el nombre del cliente: ')
###        direccion = input('Introduce la dirección del cliente: ')
###        telefono = input('Introduce el teléfono del cliente: ')
###        email = input('Introduce el correo electrónico del cliente: ')
###        vip = input('¿Es un cliente preferente (S/N)? ')
###        cliente = {'nombre':nombre, 'dirección':direccion, 'teléfono':telefono, 'email':email, 'preferente':vip=='S'}
###        clientes[curp] = cliente
###        #{'1':{'nombre':nombre, 'dirección':direccion, 'teléfono':telefono, 'email':email, 'preferente':vip=='S'},
###        #'2':{'nombre':nombre, 'dirección':direccion, 'teléfono':telefono, 'email':email, 'preferente':vip=='S'},
###        #'3':{'nombre':nombre, 'dirección':direccion, 'teléfono':telefono, 'email':email, 'preferente':vip=='S'}}
###    if opcion == '2':
###        curp = input('Introduce CURP del cliente: ')
###        if curp in clientes:
###            del clientes[curp]
###        else:
###            print('No existe el cliente con el CURP', curp)
###    if opcion == '3':
###        curp = input('Introduce CURP del cliente: ')
###        if curp in clientes:
###            print('CURP:', curp)
###            for clave, valor in clientes[curp].items():
###                print(clave.title() + ':', valor)
###        else:
###            print('No existe el cliente con el CURP', curp)
###    if opcion == '4':
###        print('Lista de clientes')
###        print(clientes)
###        print('\n\n\n')
###        #for clave, valor in clientes.items():
###        #    print(clave, valor['nombre'])
###    if opcion == '5':
###        print('Lista de clientes preferentes')
###        for clave, valor in clientes.items():
###            if valor['preferente']:
###                print(clave, valor['nombre'])
###    opcion = input('Menú de opciones\n(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Listar clientes\n(5) Listar clientes preferentes\n(6) Terminar\nElige una opción:')