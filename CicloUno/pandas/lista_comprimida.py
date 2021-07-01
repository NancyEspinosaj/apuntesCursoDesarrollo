import pandas as pd
import random

"""La comprensión de listas comúnmente conocida como 
*List Comprehension* es una manera de crear listas recorriendo 
un objeto (listas, diccionarios, etc..) de forma limpia y rápida
y lo más importante de todo es que tan solo ocupará una línea,
lo cual también hacer que sea más fácil de leer.

Las list comprehension funcionan como un bucle For, bueno, 
en realidad son un bucle For comprimido 
en una sola línea, veamos su estructura:

"""

# Método tradicional
lista = []
for letra in 'El Quijote de La Mancha':
    lista.append(letra)
print(lista)

#lista comprimida
lista = [letra for letra in 'El Quijote de La Mancha'] 
# te ahorras el append.
# el iniciar una lista vacía
print(lista)


#Estructura
lista = ['lo que va en el append' for dato in lista]


data_frame = pd.read_csv('https://s3-eu-west-1.amazonaws.com/shanebucket/downloads/uk-500.csv')
numeros_aleatorios = [random.randint(0,1000) for x in range(data_frame.shape[0])]
print(numeros_aleatorios)

numeros_aleatorios = []
for x in range(data_frame.shape[0]):
    numeros_aleatorios.append(random.randint(0,1000))
print(numeros_aleatorios)
