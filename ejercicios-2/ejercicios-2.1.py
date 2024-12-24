#falto el profe y los pibes van a armar la clase.
'''
#funciòn para obtener al asistente y al profesor segun la edad.
def obtener_compañeros(cantidad_de_compañeros):
    
    #creando la lista con los compañeros
    compañeros = []
    
    #ejecutando un for para pedir informaciòn de cada compañero
    for i in range(cantidad_de_compañeros):
        nombre = input("ingrese el nombre del compañero: ")
        edad = int(input("ingrese la edad del compañero: "))
        compañero = (nombre,edad)
        
        #agregando la informaciòn a la lista
        compañeros.append(compañero)

    #ordenandolos de menor a mayor segùn su edad   
    compañeros.sort(key=lambda x:x[1])
    
    #compañeros[x] devuelve una tupla con (nombre,edad) y despues accedemos al nombre
    #para definir al asistente y al profesor.
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    
    #retornamos una tupla
    return asistente,profesor

#desempaquetamos lo que nos retorna la funciòn
asistente,profesor = obtener_compañeros(int(input("Cantidad de alumnos: ")))

#mostrando el resultado
print(f"El profesor es: {profesor} y su asistente es {asistente}")
    
'''
'''
def mostrar_edad_por_nombre(nombre_buscado):
    if nombre_buscado in diccionario["nombres"]:
        # Encontramos el índice del nombre en la lista
        index = diccionario["nombres"].index(nombre_buscado)
        edad = diccionario["edades"][index]
        return edad
    else:
        print('Ese nombre no existe en la lista')
        return None

diccionario = {
    "nombres": [],
    "edades": []
}

condicion = True

while condicion:
    try:
        nombre = input('Colocar nombre de persona: ')
        edad = int(input('Colocar edad de persona: '))
        
        diccionario["nombres"].append(nombre)
        diccionario["edades"].append(edad)

        # Preguntamos si el usuario quiere seguir agregando personas
        continuar = input('¿Quieres agregar otra persona? (s/n): ').lower()
        if continuar != 's':
            condicion = False

    except ValueError:
        print("Hubo un error al cargar un dato. Asegúrate de ingresar una edad válida.")

# Ahora, preguntar por un nombre para mostrar su edad
nombre_buscado = input("¿Qué persona quieres buscar por nombre? ")
edad = mostrar_edad_por_nombre(nombre_buscado)

if edad is not None:
    print(f'La edad de {nombre_buscado} es {edad}.')

'''

'''
lista = [1,43,65,435,2,34,43]

lista.sort()

print(lista)
'''

