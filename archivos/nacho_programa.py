import pandas as pd

#programa que pide el nombre y apellido de una persona y si existe en el archivo, te dice la edad

def condicion():  
        df = pd.read_csv("Curso_De_Python\\archivos\\datos.csv")
        #eliminando las filas con datos faltantes
        df = df.dropna()
        #eliminando las filas repetidas
        df = df.drop_duplicates(subset=['nombre', 'apellido'], keep='first')
        df_limpio = df.sort_values('apellido')
        df_limpio.to_csv("Curso_De_Python\\archivos\\datos.csv", index=False)
        #print(df_limpio)

        return df

    #buscar persona en el archivo
def Buscar_persona():
        nombre = (input('Escribir nombre: ')).lower()
        apellido = (input('Escribir apellido: ')).lower()
        try:
            indice = df[(df['nombre'] == nombre) & (df['apellido'] == apellido)].index[0]
            edad_persona_buscada = df.loc[indice,'edad']
            print(f'\nLa edad de {nombre.capitalize()} {apellido.capitalize()} es {edad_persona_buscada}\n')
        except: 
            print("\nPersona no encontrada. Intenta de nuevo\n")

def Agregar_persona():
        nombre_para_agregar = input('Agregar nombre: ')
        apellido_para_agregar = input('Agregar apellido: ')
        edad_para_agregar = input('Agregar edad de persona: ')

        nuevos_datos = {'\n''nombre': [nombre_para_agregar], 'apellido': [apellido_para_agregar], "edad": [edad_para_agregar]}
        #convierte el diccionario en data frame, donde el key es la columna y el value es la fila
        df_nuevos_datos = pd.DataFrame(nuevos_datos)
        # Agregar los nuevos datos al archivo CSV sin sobrescribir
        df_nuevos_datos.to_csv('Curso_De_Python\\archivos\\datos.csv', mode='a', header=False, index=False)
        condicion()

def Eliminar_persona():
        nombre_a_eliminar = input('Escribir nombre a eliminar: ')
        apellido_a_eliminar = input('Escribir apellido a eliminar: ')
        # Filtrar el DataFrame para eliminar las filas que coincidan con los valores especificados
        if (nombre_a_eliminar in df['nombre'].values) & (apellido_a_eliminar in df['apellido'].values):
            df_filtrado = df[~((df['nombre'] == nombre_a_eliminar) & (df['apellido'] == apellido_a_eliminar))]
            df_filtrado.to_csv('Curso_De_Python\\archivos\\datos.csv', index=False)
            condicion()
            print(f'\n{nombre_a_eliminar.capitalize()} {apellido_a_eliminar.capitalize()} eliminado correctamente\n')
        else: 
            print("\nPersona no encontrada. Intenta de nuevo\n")

df = condicion()

while True:

    print('\n-------------------------\n- 1: Buscar persona\n- 2: Agregar persona\n- 3: Eliminar persona\n- 4: Ver archivo completo\n-------------------------')
    eleccion = input('\nElegir opción: ')

    #Buscar pesona
    if eleccion == '1':
         Buscar_persona()

    # Agregar nuevos datos
    elif eleccion == '2':
        Agregar_persona()

    #Eliminar persona
    elif eleccion == '3':
        Eliminar_persona()

    #Ver todos los archivos almacenados
    elif eleccion == '4':
        df = condicion()
        print(df)

    else: 
        print('\nColocar valor correcto, volver a intentar\n')