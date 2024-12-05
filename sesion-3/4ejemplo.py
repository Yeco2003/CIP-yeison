import pandas as pd
futbo = {
    "jugador" : ["lionel messi", "cristiano ronaldo", "neimar jr"],
    "año" : ["2003", "2004","2005"],
    "nacionalidad" : ["argentina", "portugal", "brasil"],
    "goles":["37","27","35"],
}
datos = pd.DataFrame(futbo)
print (datos) # aca abrimos un diccionario con panda

print()

#de aca para abajo abrimos un archivo csv que esta almacenado en google drive
from google.colab import drive
drive.mount('/content/drive/')

archivo="/content/drive/MyDrive/california_housing_test.csv"
datos = pd.read_csv(archivo, sep=",", header = 0)
#print(datos.head(7)) #muestra las primeras filas
#print(datos.tail()) # retorna las ultimas filas
#print(datos.sample()) #retorna filas al azar

print(datos.shape) # muestra el total de filas y colomnas

print (datos.size) # muestra el total de datos filas X columnas

print (datos.info()) # muestra los valores organizados, muestra los valores no nulos

print(datos.head(7)) # muestra los primeros datos

print (datos.tail()) # muestra los ultimos datos

print (datos.sample()) # muestra una fila al azar

print (datos.describe()) # muestra un resumen de los datos y genera estadisticas

datos.columns #muestra todas las columnas que tiene el formato, todos los nombres de las columanas

datos.columns = ['latitud', 'longitud', 'housing_median_age', 'total_rooms',
       'total_bedrooms', 'population', 'households', 'median_income',
       'median_house_value'] # podemos editar los valores de las columnas, cambiar los nombres y el orden en que aparezcan 
datos.info()

datos['latitud'].count() # trae el total que hay en la columna a la cual hagamos el llamado

datos['latitud'].value_counts() # crea tablas y nos marca cauntas veces se repite un valor en todo el formato 

datos['latitude'].unique() # llama a toods las valores unicos

datos.sort_values(['latitud','longitud','median_income']) # crea diagramas de los valores que hagamos el llamado 


