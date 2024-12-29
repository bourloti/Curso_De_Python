import csv

with open('archivos\\datos.csv') as archivo:
    datos = csv.reader(archivo)
    apellidos = []

    for row in datos:
        if 'apellido' in row:
            indice = row.index('apellido')
        print(row[indice])
        apellidos.append(row[indice])

print(apellidos)


