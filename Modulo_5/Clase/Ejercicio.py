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
