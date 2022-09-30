import csv
import os
import re

# El archivo ApplicationAuditTable.csv tiene texto separado por comas donde las columnas son:
# PartitionKey,RowKey,Timestamp,ExecutionDate,ExecutionDate@type
# 1.- Agrupar por PartitionKey y crear un archivo por cada grupo que sea igual e el PartitionKey
# Es decir todas las filas que tengan en el partitionKey 0 deben formar un archivo, las que tengan 2 otro archivo
# y así por cada partitionKey
os.system('cls')
def append_document(path: str, line: str) -> None:
    try:
        with open(path, 'a') as f:
            f.write(f"line\n")
    except Exception as ex:
        raise

def print_progress(line, total) -> None:
    os.system('cls')
    print("Procesando archivo...")
    print(f'{line} de {total} líneas procesadas')

#https://www.w3schools.com/python/python_regex.asp patrones regex
def process_file(path: str) -> None:
    try:
        counter = 1
        with open(path, 'r') as f:
            #textContent = re.findall('\"(.+\n*)*\"', f.read())
            content = csv.reader(f)
            row_count = sum(1 for row in content)
            f.seek(0)
            for l in content:
                pk = l[0] if l[0] else "lineswithoutpk"
                append_document(f"C:\\temp\\Proceced Files\\{pk}.csv", ','.join(l))
                print_progress(counter, row_count)
                counter += 1
    except Exception as ex:
        print(f"Ocurrió un error al procesar el archivo: {ex}")


#print("Procesando archivo...")
#process_file(r'C:\temp\ApplicationAuditTable.csv')
#print("Finalizado")

# 2.- El archivo ApplicationAuditTable.csv tiene texto separado por comas, obtener lo siguiente:
# Cuantas lineas tiene?
# Cuantas propiedades tiene? Las propiedades son los valores separados por ",". Por ejemplo "asd,asd,asd,ad"
# la linea anterior tienene 4 propiedades
# Mostrar las letras del alfabeto/dígitos con la cantidad de veces que aparecen en el archivo
def process_file_count(path: str) -> None:
    try:
        counter = 1
        with open(path, 'r') as f:
            content = csv.reader(f)
            row_count = sum(1 for row in content)
            f.seek(0)
            property_count = sum(len(row) for row in content)
            print(f'Total líneas: {row_count:,.0f}\nPropiedades: {property_count:,.0f}')
            f.seek(0)
            characters = {}
            for l in f.read():
                characters[l] = 1 if l not in characters else characters[l] + 1
            
            print(characters)
    except Exception as ex:
        print(f"Ocurrió un error al procesar el archivo: {ex}")


print("Procesando archivo...")
process_file_count(r'C:\temp\ApplicationAuditTable.csv')
print("Finalizado")


# 3.- El archivo ApplicationAuditTable.csv tiene texto separado por comas. obtener lo siguiente:
# Cuántas palabaras tiene todo el archivo y cuántas veces se repiten cada una?
# Definir un método para encontrar palabras parecidas. Podibles métodos a utilizar:
# Que coincidan en 2 o más letras
# Que coincidan en las 2 primeras o las dos últimas letras
# Que coincidan en las 3 letras de en medio
# Esto lo que generará son conjuntos de letras parecidas, cada conjunto debe almacenarse en un archivo diferente
