"""
Es la estructura más simple que proporciona Pandas, 
y se asemeja a una columna en una hoja de cálculo de Excel.

Un objeto Series tiene dos componentes principales: 
un índice y un vector de datos. 
Ambos componentes son listas con la misma longitud. 

"""

import pandas as pd
import numpy as np


indice = range(5)
nombres = ['Nayro','Claudia','Kevin','Santiago','Kelly']
serie_ejemplo = pd.Series(index=indice, data=nombres)
# print(serie_ejemplo)
# print(serie_ejemplo[2])

# otro ejemplo
numeros = np.arange(-10,10,1) # Crear un rango de -10 a 9 contando uno a uno
serie_ejemplo = pd.Series(index=numeros, data=numeros**2) # x**2 devuelve el valor de cada elemento de x elevado al cuadrado
# print(serie_ejemplo)


