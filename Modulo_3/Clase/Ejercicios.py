from Clasecasa import casa
#Escribir una función que reciba como parámetro otra función y una lista, y devuelva otra lista con el resultado
# de aplicar la función dada a cada uno de los elementos de la lista.
#function(paraA:fn, pamb:list) pamb = ['a','b','c','d','e']
#    Aplicar la parA a los elementos de pamb
#    return el resultado
def aplica_funcion_lista(funcion, lista):
    '''Función que aplica una función a todos los elementos de una lista.

    Parámetros:
        funcion: Es una función.
        lista: Es una lista con valores que se pasarán como argumentos a funcion.
    Devuelve:
        Una lista con el resultado de aplicar la función a los valores de la lista.
    '''
    l = []
    for i in lista:
        l.append(funcion(i))
    return l

def cuadrado(n):
    return n * n

print(aplica_funcion_lista(cuadrado, [1, 2, 3, 4]))

#Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud.
#"Hola a todos equipo de VW" -> {"Hola":4, "a":1, "todos":5, ...}
def length_words(sentence):
    '''
    Función que recibe una frase y devuelve un diccionario con las palabras que contiene y su longitud.
    Parámetros:
        sentence: Es una cadena de caracteres con una frase.
    Devuelve:
        Un diccionario con pares palabra:longitud donde palabra son las palabras que contiene la frase sentence.
    '''
    words = sentence.split()
    lengths = map(len, words)
    return dict(zip(words, lengths))

print(length_words('Welcome to Python'))


#Una inmobiliaria de una ciudad maneja una lista de inmuebles como la siguiente:
#[{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A', 'precio': 23423.334},
#{'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B', 'precio': 23423.334},
#{'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A', 'precio': 23423.334},
#{'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'precio': 23423.334},
#{'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A', 'precio': 23423.334}]
#Construir una función que permita hacer búsqueda de inmuebles en función de un presupuesto dado.
# La función recibirá como entrada la lista de inmuebles y un precio, y devolverá otra lista con
# los inmuebles cuyo precio sea menor o igual al proporcionado. Debe hacerlo con clases.