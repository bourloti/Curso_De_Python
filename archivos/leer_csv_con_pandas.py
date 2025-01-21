import pandas as pd
import matplotlib

#usando la funcion read_csv para leer el archivo CSV
df = pd.read_csv("Curso-Dalto-Python\\Curso_De_Python\\archivos\\datos.csv")
print(df)

diccionario = {'nombre': ['nacho'], 'apellido': ['bourlot'], 'edad': [23]}
data_frame_nuevo = pd.DataFrame(diccionario)

data_frame_nuevo.to_csv('Curso_De_Python\\archivos\\datos.csv', mode='a')

'''
#obteniendo los datos de la columna nombre
nombres = df["nombre"]

#ordenando el dataframe por la edad
df_orden_ascendente = df.sort_values("edad")

#ordeandolo de forma descendente
df_orden_descendente = df.sort_values("edad",ascending=False)

#concatenando los 2 dataframes
df_concatenado = pd.concat([df,df2])

#accediendo a la primeras 3 filas con head()
primeras_filas = df.head(3)

#accediendo a las últimas 3 filas con tail()
ultimas_filas = df.tail(3)

#accediendo a la cantidad de filas y columnas con shape
filas_totales,columnas_totales = df.shape

#obteniendo data estadística del dataframe:
df_info = df.describe()

#obtiene todos los metodos y propiedades del archvo .csv leido
#print(dir(df))

# obtiene el promedio de edades del archivo .csv
#print(df['edad'].mean())'''

'''#accediendo a la edad de la fila 2
elemento_especifico_loc = df.loc[2,"edad"]

#accediendo a la edad de la fila 2 con iloc
elemento_especifico_iloc = df.iloc[2,2]

#accediendo a todos los apellidos con loc
apellidos_loc = df.loc[:,"apellido"]

#accediendo a todos los apellidos con iloc
apellidos = df.iloc[:,1]

#accediendo a la fila 3 con loc
fila_3 = df.loc[2,:]

#accediendo a la fila 3 con iloc
fila_3 = df.iloc[2,:]

#accediendo a filas con edad mayor que 30 con loc
mayor_que_30 = df.loc[df["edad"]>30,:]

#print(mayor_que_30)
'''
