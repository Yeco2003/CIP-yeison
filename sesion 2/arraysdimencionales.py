import numpy as np 
array = np.array ([1,2,3,4,5])
arrm = array.max() # para buscar el numero maximo 
arrn = array.min() # para buscar el numero minimo 
arras = array.sum() # para sumar todos los numeros de el array
print(f" el numero maximo es {arrm} \n el numero minimo es {arrn} \n y la suma de todos los numeros es {arras}")
print()

array_rango = array [:3] # usar rangos de los arrays 
print("el rango de arrays que has escogido es:",array_rango)
print("\n")

array [:] = 99 #agregar el numero 99 a todas las posiciones 
print(array)
