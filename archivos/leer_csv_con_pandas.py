import pandas as pd

#usando la funcion read_csv para leer el archivo CSV
df = pd.read_csv("archivos\\datos.csv")
df2 = pd.read_csv("archivos\\datos.csv")
#print(df)

#obteniendo los datos de la columna nombre
nombres = df["nombre"]
#print(nombres)

#ordenando el dataframe por la edad
df_orden_ascendente = df.sort_values("edad")
#print(df_orden_ascendente)

#ordeandolo de forma descendente
df_orden_descendente = df.sort_values("edad",ascending=False)
#print(df_orden_descendente)

#concatenando los 2 dataframes
df_concatenado = pd.concat([df,df2])
#print(df_concatenado)

#accediendo a la primeras 3 filas con head()
primeras_filas = df.head(3)
#print(primeras_filas)

#accediendo a las últimas 3 filas con tail()
ultimas_filas = df.tail(3)
#print(ultimas_filas)

#accediendo a la cantidad de filas y columnas con shape
filas_totales,columnas_totales = df.shape
#print(filas_totales,columnas_totales)

#obteniendo data estadística del dataframe:
df_info = df.describe()
#print(df_info)
#print(df_info.loc['mean','edad'])

#maximo = df_info.loc['max','edad']
#print(maximo)

#accediendo a la edad de la fila 2
elemento_especifico_loc = df.loc[:,"edad"]
#print(elemento_especifico_loc)

#accediendo a la edad de la fila 2 con iloc
elemento_especifico_iloc = df.iloc[2,2]
#print(elemento_especifico_iloc)

#accediendo a todos los apellidos con loc
apellidos_loc = df.loc[:,"apellido"]
#print(apellidos_loc)

#accediendo a todos los apellidos con iloc
apellidos = df.iloc[:,1]
#print(apellidos)

#accediendo a la fila 3 con loc
fila_3 = df.loc[2,:]
#print(fila_3)

#accediendo a la fila 3 con iloc
fila_3 = df.iloc[2,:]

#accediendo a filas con edad mayor que 30 con loc
mayor_que_30 = df.loc[df["edad"]>30,:]
#print(mayor_que_30)

#buscando algunos valores dentro de una columna
print(dir(df))

edad_maxima = df['edad'].max()
edad_minima = df['edad'].min()
promedio_edades = df['edad'].mean()
print(f'{edad_maxima},{edad_minima},{promedio_edades}')

resultado = df['edad'][(df['nombre'] == 'nicolas') & (df['apellido'] == 'zosten')]
resultado 
print(resultado)