#hacer una serie de fibonacci arrancando de cualquier valor

'''def serie(valor, hasta):
    valor1 = 0
    lista = []
    while valor1 < hasta:
        lista.append(valor1)
        print(valor1)
        valor1 = valor + valor1
        valor = valor1 - valor
        if valor1 > hasta:
            break
        
    return lista

print(serie(70,4000))'''

'''def serie(num):
    num1, num2 = 0,1
    lista = []
    while num1 < num:
        lista.append(num1)
        num2 = num1 + num2
        num1 = num2 - num1
    return lista

print(serie(4000))'''

'''# Creamos un diccionario con claves 'nombres' y 'edades'
personas = {
    'nombres': [],
    'edades': []
}

# Bucle para ingresar varios datos
while True:
    # Solicitamos el nombre
    nombre = input("Ingresa el nombre de la persona (o 'salir' para terminar): ")
    
    # Si el usuario ingresa 'salir', salimos del bucle
    if nombre.lower() == 'salir':
        break
    
    # Solicitamos la edad, asegurándonos de que sea un número
    edad = input(f"Ingresa la edad de {nombre}: ")
    
    # Verificamos si la edad es un número válido
    if edad.isdigit():
        # Agregamos el nombre y la edad a las listas correspondientes
        personas['nombres'].append(nombre)
        personas['edades'].append(int(edad))
    else:
        print("Por favor, ingresa una edad válida (número entero).")

# Ahora pedimos un nombre para mostrar su edad
nombre_buscado = input("\nIngresa el nombre de la persona para ver su edad: ")

# Verificamos si el nombre está en la lista de nombres
if nombre_buscado in personas['nombres']:
    # Encontramos el índice del nombre en la lista
    index = personas['nombres'].index(nombre_buscado)
    print(f"La edad de {nombre_buscado} es {personas['edades'][index]} años.")
else:
    print(f"No se encontró a {nombre_buscado} en el registro.")'''


lista = [1,34,23,543,534,43]
diccionario = {
    'nombre': [],
    'edad': []
}

while True:
    try:
        diccionario['nombre'].append(input('agregar nombre: '))
        diccionario['edad'].append(int(input('agregar nombre: ')))
        if input('queres salir: ') == 'salir':
            break
    except:
        print(diccionario)

persona_buscada = input('buscar persona: ')

if persona_buscada in diccionario['nombre']:
    index = diccionario['nombre'].index(persona_buscada)
    edad = diccionario['edad'][index]
    print(f'la edad de {persona_buscada} es {edad}')

print(lista[4])