import numpy as np
np.array([[1,2],[3,4],[5,6]])
# axis el 0 es de columna el 1 es de filas
array_multidimencional = np.array([[1,2,3,4],[4,5,6,7]])
print(array_multidimencional)
print()
array_multidimencional3 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) # creamos array con tres columnas y cuatro filas cada una
print (array_multidimencional3)
print()
array_multidimencional3 [0][0:3] #con esta muestro la fila que quiero que se muestre, y el valor que quiero que se muestre
array_columna=array_multidimencional3 [:2,0:3] # llama las filas que quiero que se haga el llamado y llamo desde que columna quiero obtener los valores
print(array_columna)
print()
arraymax=array_multidimencional3.max() #el numero mayor de la matrix
arrayresta=array_multidimencional3.min() # el numero menor de la matrix
arraysuma=array_multidimencional3.sum() # la suma de todos los numeros de la matrix
arraymaxaxis=array_multidimencional3.max(axis=0) # los numeros mayores de las columnas - filas
arrayminaxis=array_multidimencional3.min(axis=1) # los numeros menores de las colomnas - filas
arraysumaxis=array_multidimencional3.sum(axis=0) # la suma de los numeros de las columnas - filas
array_multidimencional3 [2].max()# el numero maximo de la columna 2, se puede hacer con min y sum
