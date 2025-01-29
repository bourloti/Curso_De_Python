import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

# Leer el archivo CSV
df = pd.read_csv('./Curso_De_Python/analisis_trending/Trending_planta_parboil.csv', sep=';')  # Ajusta el nombre del archivo y el separador si es necesario

columna_tiempo = 'Ingreso Silo 101 Time'
columna_caudal = 'Ingreso Silo 101'

df[columna_tiempo] = df[columna_tiempo].replace({'a.m.': 'AM', 'p.m.': 'PM'}, regex=True)
# Convertir la columna 'Fecha y Hora' a formato datetime
df[columna_tiempo] = pd.to_datetime(df[columna_tiempo], format='%d/%m/%Y %I:%M:%S %p')
#print(df[columna_tiempo])

df[columna_caudal] = df[columna_caudal].str.replace(',', '.', regex=False)
df[columna_caudal] = pd.to_numeric(df[columna_caudal])

# Eliminar las filas donde todos los valores sean 0
#df = df[df[columna_caudal] != 0.0]

# Filtrar los datos para que solo queden dentro del rango esperado
df = df[df[columna_caudal].between(0,25)]

#df_nuevo = pd.DataFrame({'fecha_silo_101': df['Ingreso Silo 101 Time'], 'silo_101': df['Ingreso Silo 101']})
df_nuevo = pd.DataFrame({'fecha_silo_101': df[columna_tiempo], 'silo_101': df[columna_caudal]})

lista_1 = []
lista_2 = []
dia = '20/12/2024'

# Iterar de 12 a 11 pm (24 horas)
for i in range(24):  
    
    if i < 23:
        # Crear las horas de inicio y fin en formato 24 horas
        hora_inicio = f'{dia} {i:02d}:00:00'
        hora_fin = f'{dia} {(i+1)%24:02d}:00:00'
    else:
        # Crear las horas de inicio y fin en formato 24 horas
        hora_inicio = f'{dia} {i:02d}:00:00'
        hora_fin = f'{dia} 23:59:00'

    # Filtrar el DataFrame para las filas que están entre hora_inicio y hora_fin
    df_filtrado = df_nuevo[df_nuevo['fecha_silo_101'].between(hora_inicio, hora_fin)]

    # Calcular el promedio de las columnas numéricas en ese rango horario
    promedio_por_hora = df_filtrado['silo_101'].mean()  # Esto devuelve una Serie con el promedio de cada columna numérica

    lista_1.append(pd.to_datetime(f'{dia} {i:02d}:00:00', format='%d/%m/%Y %H:%M:%S'))
    lista_2.append(promedio_por_hora)

    # Acumular los promedios por hora
    if i == 0:
        toneladas_en_dia = promedio_por_hora
    else:
        toneladas_en_dia = toneladas_en_dia + promedio_por_hora
        
    if i == 23:
        df_final = pd.DataFrame({'fecha': lista_1, 'totalizador': lista_2})

# Crear el gráfico de barras
plt.figure(figsize=(10, 6))

# Dibujar las barras en el gráfico, donde el eje X es la fecha de inicio de cada intervalo
plt.bar(df_final['fecha'], df_final['totalizador'], width=0.02)  # width ajusta el tamaño de las barras

# Configurar el formato de fecha en el eje X
plt.gca().xaxis.set_major_formatter(DateFormatter('%H:%M'))

# Ajustar el formato de las etiquetas en el eje X para que no se solapen
plt.xticks(rotation=90, ha='right')

# Añadir etiquetas y título
plt.xlabel('Fecha: 17/12/2024')
plt.ylabel('Total por hora')
plt.title(f'Caudal entre Intervalos de Tiempo. Toneladas totales en el dia {toneladas_en_dia}')

# Mostrar el gráfico
plt.tight_layout()  # Ajusta los márgenes
plt.show()