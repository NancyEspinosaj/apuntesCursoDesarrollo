import pandas as pd
from pandas.core.frame import DataFrame
from dotenv import load_dotenv
import os

load_dotenv()
ruta = os.getenv("RUTA")

"""
Un DataFrame es una estructura de datos con dos dimensiones en la cual 
se puede guardar datos de distintos tipos en columnas
Es similar a una hoja de cálculo o una tabla de SQL o el data.frame de R. 
Un DataFrame siempre tiene un índice (con inicio en 0). 

El índice refiere a la posición de un elemento en la estructura de datos.
El índice contiene valores únicos y, por lo general, ordenados, 
y se usa para acceder a valores individuales de los datos.

"""


data_frame = pd.read_csv(ruta, header=1)
primeros_datos = data_frame.head()
print(primeros_datos)
# primeros_datos

# para ver una columna
print(data_frame['Period'])

# para ver las columnas
columnas = list(data_frame.columns)
print(columnas)