x = True
y = False
print(x or y)

print(x and y)

print(not x)

x = 0
y = 10
print(x or y)

print(x and y)

print(not x)

##########################################################################
x = 9
y = 1
print(x < y)
print(x > y)
print(x == y)

# Las comparaciones siguientes son idénticas
x = 9
print(1 < x and x < 20)
print(1 < x < 20)

##############################################################################
x = 7
y = 2
print(x + y)  # Suma
print(x - y)  # Resta
print(x * y)  # Producto
print(x / y)  # División
print(x % y)  # módulo
print(x // y)  # Cociente
print(x ** y)  # Potencia

##############################################################################
lista = [1, 3, 2, 7, 9, 8, 6]
print(4 in lista)
print(3 in lista)
print(4 not in lista)

x = 4
y = 2
lista = [1, 5]
print(x is lista)
print(x is y)
print(x is 4)

#################################################
cadena = input("Captura una cadena por favor")
print(cadena)

entero = input("Capture un número entero")
print(entero)
print(int(entero))

flotante = input("Capture un número flotante")
print(flotante)
print(int(flotante))