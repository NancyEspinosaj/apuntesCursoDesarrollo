import pandas as pd
import random
 
# descargamos un csv
data_frame = pd.read_csv('https://s3-eu-west-1.amazonaws.com/shanebucket/downloads/uk-500.csv')
# nos inventamos los id
data_frame['id'] = [random.randint(0,1000) for x in range(data_frame.shape[0])]
 
print(data_frame.head(5))


# selección usando iloc
# seleccionar por posición

# Filas:
primera_fila = data_frame.iloc[0] 
segunda_fila = data_frame.iloc[1] 
ultima_fila = data_frame.iloc[-1]
# print(ultima_fila)

# Columnas:
primer_columna = data_frame.iloc[:,0] 
segunda_columna = data_frame.iloc[:,1] 
ultima_columna = data_frame.iloc[:,-1]
print(primer_columna)

# Selección multiple de filas y columnas usando iloc y DataFrame
primeras_cinco_filas = data_frame.iloc[0:5] 
primeras_dos_columnas_todas_filas = data_frame.iloc[:, 0:2]
filas_columnas_seleccionadas = data_frame.iloc[[0,3,6,24], [0,5,6]]
primeras_cinco_filas_columnas_seleccionadas = data_frame.iloc[0:5, 5:8]
print(primeras_cinco_filas_columnas_seleccionadas)
