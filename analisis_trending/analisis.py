import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

# Leer el archivo CSV
df = pd.read_csv('./Curso_De_Python/analisis_trending/Trending_planta_parboil.csv', sep=';')  # Ajusta el nombre del archivo y el separador si es necesario

df['Ingreso Silo 101 Time'] = df['Ingreso Silo 101 Time'].replace({'a.m.': 'AM', 'p.m.': 'PM'}, regex=True)

# Convertir la columna 'Fecha y Hora' a formato datetime
df['Ingreso Silo 101 Time'] = pd.to_datetime(df['Ingreso Silo 101 Time'], format='%d/%m/%Y %I:%M:%S %p')

df['Ingreso Silo 101'] = df['Ingreso Silo 101'].str.replace(',', '.', regex=False)

df['Ingreso Silo 101'] = pd.to_numeric(df['Ingreso Silo 101'])

# Filtrar los datos para que solo queden dentro del rango esperado (por ejemplo, entre 0 y 50)
df = df[(df['Ingreso Silo 101'] >= 0) & (df['Ingreso Silo 101'] <= 25)]

df_nuevo = pd.DataFrame({'fecha_silo_101': df['Ingreso Silo 101 Time'], 'silo_101': df['Ingreso Silo 101']})

print(df_nuevo)

# Definir las fechas de inicio y fin que quieres filtrar
fecha_inicio = '16/12/2024 11:02:28 p.m.'
fecha_fin = '16/12/2024 11:12:28 p.m.'

# Filtrar el DataFrame entre esas fechas
df_filtrado = df_nuevo[(df_nuevo['fecha_silo_101'] >= fecha_inicio) & (df_nuevo['fecha_silo_101'] <= fecha_fin)]

# Mostrar el DataFrame filtrado
print(df_filtrado.mean())
print(df_filtrado)
#print(dir(df_filtrado))


# Graficar la temperatura en función de la fecha y hora
plt.figure(figsize=(10, 6))
#plt.plot(df['Ingreso Silo 101 Time'], df['Ingreso Silo 101'], marker='o', linestyle='-', color='b')
plt.plot(df_filtrado['fecha_silo_101'],df_filtrado['silo_101'], marker='o', linestyle='-', color='b')

# Personalizar la gráfica
plt.title('Serie Temporal de Temperaturas', fontsize=10)
plt.xlabel('Fecha y Hora', fontsize=8)
plt.ylabel('Temperatura (°C)', fontsize=12)

# Ajustar el formato de las fechas en el eje X (incluir la hora)
date_format = DateFormatter('%d/%m/%Y %H:%M')  # Día/Mes/Año Hora:Minuto:Segundo
plt.gca().xaxis.set_major_formatter(date_format)

plt.xticks(rotation=45)  # Rotar las etiquetas del eje X para mejor visibilidad
plt.grid(True)

# Mostrar la gráfica
plt.tight_layout()
plt.show()

'''
import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV
df = pd.read_csv('./Curso_De_Python/analisis_trending/datos_temperatura.csv', sep=';')  # Ajusta el nombre del archivo y el separador si es necesario

# Convertir la columna 'Fecha y Hora' a formato datetime
df['Fecha y Hora'] = pd.to_datetime(df['Fecha y Hora'], format='%d/%m/%Y %I:%M:%S %p')

# Graficar la temperatura en función de la fecha y hora
plt.figure(figsize=(10, 6))
plt.plot(df['Fecha y Hora'][50:100], df['Temperatura (°C)'][50:100], marker='o', linestyle='-', color='b')

# Personalizar la gráfica
plt.title('Serie Temporal de Temperaturas', fontsize=14)
plt.xlabel('Fecha y Hora', fontsize=12)
plt.ylabel('Temperatura (°C)', fontsize=12)
plt.xticks(rotation=45)  # Rotar las etiquetas del eje X para mejor visibilidad
plt.grid(True)

# Mostrar la gráfica
plt.tight_layout()
plt.show()
print(df['Temperatura (°C)'][50:100])'''