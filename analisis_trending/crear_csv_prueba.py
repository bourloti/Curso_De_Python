import random
import csv
from datetime import datetime, timedelta

# Función para generar 200 puntos de datos y guardarlos en un archivo CSV
def generar_datos_csv():
    # Hora de inicio
    start_time = datetime(2024, 12, 16, 0, 0, 0)
    
    # Lista para almacenar los datos
    datos = []
    
    for _ in range(200):
        # Incrementar el tiempo en minutos aleatorios
        random_minutes = random.randint(1, 30)
        start_time += timedelta(minutes=random_minutes)
        
        # Temperatura aleatoria entre 0 y 20 grados
        temperatura = round(random.uniform(0, 20), 2)
        
        # Formatear el tiempo en el formato requerido
        formatted_time = start_time.strftime("%d/%m/%Y %I:%M:%S %p")
        
        # Guardar los datos en una lista
        datos.append([formatted_time, temperatura])
    
    # Escribir los datos en un archivo CSV con punto y coma como delimitador
    with open('datos_temperatura.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=';')
        
        # Escribir la cabecera
        writer.writerow(['Fecha y Hora', 'Temperatura (°C)'])
        
        # Escribir los datos
        writer.writerows(datos)

# Llamar la función para generar los datos y guardar el archivo CSV
generar_datos_csv()
