import pandas as pd
import random
 
# descargamos un csv
data_frame = pd.read_csv('https://s3-eu-west-1.amazonaws.com/shanebucket/downloads/uk-500.csv')
# nos inventamos los id
data_frame['id'] = [random.randint(0,1000) for x in range(data_frame.shape[0])]
#lista comprimida


# print(data_frame.head(5))

# selección usando loc
# por etiquetas o condiciones.

data_frame.set_index("last_name", inplace=True)
# print(data_frame.head(5))

apellido_andrade = data_frame.loc['Andrade']
apellido_andrade_zigomalas = data_frame.loc[['Andrade','Zigomalas']]

# print(apellido_andrade_zigomalas)

#si solo quiero conocer su nombre, dirección y ciudad
datos_andrade_zigomalas = data_frame.loc[['Andrade','Zigomalas'],['first_name','address','city']]

# print(datos_andrade_zigomalas)

# los que están entre Salvadore y Molaison
datos_entre_Salvadore_Molaison = data_frame.loc['Salvadore':'Molaison',['first_name','address','city']]
# print(datos_entre_Salvadore_Molaison)

# Todas las columnas desde ciudad hasta email
desde_ciudad_hasta_email = data_frame.loc[['Salvadore','Molaison'],'city':'email']
# print(desde_ciudad_hasta_email)

#cambiar de indice
data_frame.set_index('id',inplace=True)
print (data_frame.head(5))
