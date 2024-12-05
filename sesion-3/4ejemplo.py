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
