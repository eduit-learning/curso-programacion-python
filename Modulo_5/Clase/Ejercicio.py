#El archivo ApplicationAuditTable.csv tiene texto separado por comas donde las columnas son:
#PartitionKey,RowKey,Timestamp,ExecutionDate,ExecutionDate@type
#1.- Agrupar por PartitionKey y crear un archivo por cada grupo que sea igual e nel PartitionKey
#Es decir todas las filas que tengan en el partitionKey 0 deben formar un archivo, las que tengan 2 otro archivo
# y así por cada partitionKey

#2.- El archivo ApplicationAuditTable.csv tiene texto separado por comas, obtener lo siguiente:
#Cuantas lineas tiene?
#Cuantas propiedades tiene? Las propiedades son los valores separados por ",". Por ejemplo "asd,asd,asd,ad"
#la linea anterior tienene 4 propiedades
#Mostrar las letras del alfabeto/dígitos con la cantidad de veces que aparecen en el archivo

#3.- El archivo ApplicationAuditTable.csv tiene texto separado por comas. obtener lo siguiente:
#Cuántas palabaras tiene todo el archivo y cuántas veces se repiten cada una?
#Definir un método para encontrar palabras parecidas. Podibles métodos a utilizar:
# Que coincidan en 2 o más letras
# Que coincidan en las 2 primeras o las dos últimas letras
# Que coincidan en las 3 letras de en medio
#Esto lo que generará son conjuntos de letras parecidas, cada conjunto debe almacenarse en un archivo diferente
