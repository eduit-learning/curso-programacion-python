d = {1: 'hola', 89: 'Python', 'a': 'b', 'c': 27}

# 1. Pares clave: valor encerrados entre llaves
d = {'uno': 1, 'dos': 2, 'tres': 3}
print(d)

# 2. Argumentos con nombre
d2 = dict(uno=1, dos=2, tres=3)
print(d2)

# 3. Pares clave: valor encerrados entre llaves
d3 = dict({'uno': 1, 'dos': 2, 'tres': 3})
print(d3)

# 4. Iterable que contiene iterables con dos elementos
d4 = dict([('uno', 1), ('dos', 2), ('tres', 3)])
print(d4)

# 5. Diccionario vacío
d5 = {}
print(d5)

# 6. Diccionario vacío usando el constructor
d6 = dict()
print(d6)

d = {'uno': 1, 'dos': 2, 'tres': 3}
print(d.get('uno'))


# Devuelve 4 como valor por defecto si no encuentra la clave
print(d.get('cuatro', 4))

# Devuelve None como valor por defecto si no encuentra la clave
a = d.get('cuatro')
print(a)
print(type(a))

############################################################################################
d = {'uno': 1, 'dos': 2, 'tres': 3}
for e in d:
    print(e)

# Recorrer las claves del diccionario
for k in d.keys():
    print(k)

# Recorrer los valores del diccionario
for v in d.values():
    print(v)

# Recorrer los pares clave valor
for i in d.items():
    print(i)

############################################################################################ - recorrer
d = {'uno': 1, 'dos': 2, 'tres': 3}
for e in d:
    print(e)

# Recorrer las claves del diccionario
for k in d.keys():
    print(k)

# Recorrer los valores del diccionario
for v in d.values():
    print(v)

# Recorrer los pares clave valor
for i in d.items():
    print(i)

d = {'uno': 1, 'dos': 2}
print(d.setdefault('uno', 1.0))
print(d.setdefault('tres', 3))
d.setdefault('cuatro')
print(d)

############################################################################################ - Modificar
d = {'uno': 1, 'dos': 2}
print(d)

d['uno'] = 1.0
print(d)

############################################################################################# - Eliminar
d = {'uno': 1, 'dos': 2, 'tres': 3, 'cuatro': 4, 'cinco': 5}

# Elimina un elemento con pop()
print(d.pop('uno'))
print(d)

# Trata de eliminar una clave con pop() que no existe
print(d.pop(6))

# Elimina un elemento con popitem()
print(d.popitem())
print(d)

# Elimina un elemento con del
del d['tres']
print(d)

# Trata de eliminar una clave con del que no existe
del d['seis']

# Borra todos los elementos del diccionario
d.clear()
print(d)

############################################################################################# - N+umero de elementos
d = {'uno': 1, 'dos': 2, 'tres': 3}
print(len(d))

############################################################################################# - Validar si un elemento está
print('uno' in d)
print(1 in d)
print(1 not in d)

# Intenta eliminar la clave 1 si existe
if 1 in d:
    del d[1]    
print(d)

############################################################################################# - Comparación
d1 = {'uno': 1, 'dos': 2}
d2 = {'dos': 2, 'uno': 1}
d3 = {'uno': 1}
print(d1 == d2)
print(d1 == d3)
print(d1 > d2)#Error

############################################################################################# - Dic anidados
d = {'d1': {'k1': 1, 'k2': 2}, 'd2': {'k1': 3, 'k4': 4}}
print(d['d1']['k1'])
print(d['d2']['k1'])
print(d['d2']['k4'])
print(d['d3']['k4'])#error

############################################################################################# - Convertir en lista
d = {'uno': 1, 'dos': 2, 'tres': 3}
print(list(d))