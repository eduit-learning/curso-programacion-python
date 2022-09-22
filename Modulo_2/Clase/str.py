s = 'Hola Python'
print(s)
print(type(s))

s2 = "Me gusta Python"
print(s2)
print(type(s2))

########################################################### - for
saludo = 'Hola'
for c in saludo:
    print(c)

saludo = 'Hola'
print('o' in saludo)
print('p' in saludo)
print('p' not in saludo)

############################################################ - Comprobar si dos string son iguales
s1 = 'hola'
s2 = 'hola'
print(s1 == s2)

s3 = 'Hola'
print(s1 == s3)

saludo = 'Hola'
print(len(saludo))

############################################################ - Comprobar si una cadena está vacía
def is_empty(data_structure):
    if data_structure:
        print("No está vacía")
        return False
    else:
        print("Está vacía")
        return True
d = {}
t = ()
l = []
str = ''
s = set()

print(is_empty(d))
print(is_empty(t))
print(is_empty(l))
print(is_empty(str))
print(is_empty(s))

d['a'] = 1
t = tuple('a')
l.append('a')
str = 'a'
s.add('a')

print(is_empty(d))
print(is_empty(t))
print(is_empty(l))
print(is_empty(str))
print(is_empty(s))

############################################################ - Concatenación
nombre = 'Pedro'
apellidos = 'Pérez Penas'
nombre_completo = nombre + apellidos
print(nombre_completo)

suma = 1 + 2
print(suma)
res = 'El resultado de 1 + 2 es: ' + suma #Error solo se puede concatenar cadenas

suma = 1 + 2
print(suma)
res = 'El resultado de 1 + 2 es: ' + str(suma)
print(res)

#Format
nombre = 'Pedro'
print('Hola %s' % nombre)

def print_suma(x, y):
    return 'El resultado de %i e %i es: %i' % (x, y, x+y)
print_suma(1, 2)

var1 = 'Pedro'
var2 = 'Hola'
print('{} {}, ¿cómo estás?'.format(var2, var1))

var1 = 'Pedro'
var2 = 'Hola'
print('{var2} {var1}, ¿cómo estás?'.format(var1=var1, var2=var2))

var1 = 'Pedro'
var2 = 'Hola'
print('{1} {0}, ¿cómo estás?'.format(var1, var2))

#A partir de Python 3.6
nombre = 'Pedro'
print(f'Hola {nombre}')

cadenas = ['Hola', 'j2logo', ',', '¿cómo', 'estás?']
print(' '.join(cadenas))

numeros = ['1', '2', '3']
print(', '.join(numeros))

#################################################################################33 - Replace
dir_name = 'S2A_MSIL1C_20190106T105431_N0207_R051_T30SXH_20190106T112304'
new_dir_name = dir_name.replace('MSIL1C', 'MSIL2A')
print(new_dir_name)

aes = 'aaaaaa'
nueva = aes.replace('a', 'b', 3)
print(nueva)

#################################################################################33 - Eliminar espacios en blanco
hola = ' \t\t\n\tHola \n '
print(hola)

hola_limpio = hola.strip()
print(hola_limpio)

texto = ' hola mundo hola \ni'
print(texto.strip(' oahl'))
print(texto.strip(' \nioahl'))

hola = ' hola '
print(hola.rstrip())
print(hola.lstrip())

#################################################################################33 - Mayúsculas y minúsculas
hola = 'Hola python'
hola_upper = hola.upper()
print(hola)
print(hola_upper)

hola = 'HOLA Python'
hola_lower = hola.lower()
print(hola)
print(hola_lower)

print('hola python. ¿te gusta python?'.capitalize())

hola = 'Hola Python. ¿Te gusta Python?'
hola_swaped = hola.swapcase()
print(hola)
print(hola_swaped)

hola = 'hola pythonista. ¿te gusta python?'
hola_title = hola.title()
print(hola)
print(hola_title)

print('Hola'.isupper())
print('HOLA'.isupper())

print('Hola'.islower())
print('hola'.islower())

#################################################################################33 - Split
print('  Me    gusta \t\nPython     '.split())
print('  Me    gusta \t\nPython     '.split(' '))
print('1,2,3'.split(sep=','))
print('1, 2, 3'.split(sep=', '))
print('1,,2,,,3'.split(','))

print('Me gusta Python'.split(maxsplit=1))
print('1, 2, 3, 4, 5'.split(sep=', ', maxsplit=2))