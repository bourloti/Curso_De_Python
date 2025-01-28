import pandas as pd
import matplotlib.pyplot as plt

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


'''lista = [1,34,23,543,534,43]
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

print(lista[4])'''

'''df = pd.read_csv('Curso_De_Python\\Trending_planta_parboil.csv',sep=';')'''

'''df_time_ingreso_silo_101 = pd.to_datetime(df['Ingreso Silo 101 Time'], errors='coerce')
df_ingreso_silo_101 = pd.to_numeric(df['Ingreso Silo 101'], errors='coerce')

df_time_ingreso_materia_prima = pd.to_datetime(df['Ingreso Materia Prima Time'], errors='coerce')
df_ingreso_ingreso_materia_prima = pd.to_numeric(df['Ingreso Materia Prima'], errors='coerce')

df_time_descarte_zaranda = pd.to_datetime(df['Descarte Zaranda Time'], errors='coerce')
df_descarte_zaranda = pd.to_numeric(df['Descarte Zaranda'], errors='coerce')

df_time_tempering = pd.to_datetime(df['Ingreso Silo de tempering Time'], errors='coerce')
df_tempering = pd.to_numeric(df['Ingreso Silo de tempering'], errors='coerce')

# Asegurarse de que la columna de fecha sea del tipo datetime
plt.plot(df_time_ingreso_silo_101, df_ingreso_silo_101)
plt.title('Valor a lo largo del tiempo')
plt.xlabel('Fecha')
plt.ylabel('Valor')
plt.xticks(rotation=45)
plt.show()
'''
'''# Leer el archivo CSV con el delimitador correcto
df = pd.read_csv('Curso_De_Python\\Trending_planta_parboil.csv', delimiter=';', encoding='latin1')

# Verificar las primeras filas para asegurarnos de que se lee correctamente
#print(df.head())

# Convertir las fechas usando el formato adecuado
df_time_ingreso_silo_101 = pd.to_datetime(df['Ingreso Silo 101 Time'], format= '%d/%m/%Y %I:%M:%S %p', errors='coerce')
# Verificar si hay NaT (Not a Time)
print(df_time_ingreso_silo_101.isna().sum())  # Muestra cuántas fechas no se han podido convertir'''


'''df = pd.read_csv('Curso_De_Python\\archivos\\datos.csv')

df['edad'] = df['edad'].astype(str)
print(type(df['edad'][0]))'''

'''datos_nuevos = {'nombre': ['nacho', 'lean', 'santi'], 'apellido': ['bourlot','bourlot','bourlot'], 'edad': [23,24,25]}

df = pd.DataFrame(datos_nuevos)
print(df)
df.to_csv('Curso_De_Python\\archivos\\datos_nuevos.csv')'''

'''class Celular:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        
    def llamar(self):
        print(f'El celular {self.marca} modelo {self.modelo} del año {self.año} esta llamando')
        
celular1 = Celular('Iphone', '11 Pro', '2020')
celular2 = Celular('Nokia', '1100', '2005')

celular2.llamar()'''

'''class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def estudiar(self):
        print(f'El estudienate {self.nombre} esta estudiando')

condicion = True

while condicion:
    nombre_estudiante = input('Colocar nombre de estudiante: ')
    edad_estudiante = input('Colocar edad de estudiante: ')
    grado_estudiante = input('Colocar grado de estudiante: ')

    poner_a_estudiar = input('Poner al estudiante a estudiar?: ').lower()

    estudiante = Estudiante(nombre_estudiante, edad_estudiante, grado_estudiante)

    if poner_a_estudiar == 'estudiar':
        estudiante.estudiar()
        condicion = False
        '''
        
'''class Persona:
    def __init__(self, nombre, edad, pais):
        self.nombre = nombre
        self.edad = edad
        self.pais = pais
    
    def hablar(self):
        print('Estoy hablando')

class Empleado(Persona):
    def __init__(self, nombre, edad, pais, sector, numero_operario):
        super().__init__(nombre, edad, pais)
        self.sector = sector
        self.numero_operario = numero_operario
        
empleado_1 = Empleado('nacho', '27', 'Argentina', 'Mantenimiento', 2020)

print(empleado_1.sector)    
empleado_1.hablar()
        '''

'''class Persona:
    def __init__(self, nombre, edad, pais):
        self.nombre = nombre
        self.edad = edad
        self.pais = pais
        
class Artista:
    def __init__(self, habilidad = 'Basquet'):
        self.habilidad = habilidad
        
    def mostrar_habilidad(self):
        return f'La habilidad es {self.habilidad}'
        
        
class PersonaArtisita(Persona, Artista):
    def __init__(self, nombre, edad, pais, habilidad, sector):
        Persona.__init__(self, nombre, edad, pais)
        Artista.__init__(self, habilidad)
        self.sector = sector
        
    def funcion(self):
        return f'{self.nombre} con la habilidad de {self.habilidad} trabaja en el sector {self.sector}. {super().mostrar_habilidad()}'

persona_1 = PersonaArtisita('Nacho', '27', 'Argentina', 'Futbol', 'Mante')

print(persona_1.funcion())'''

'''#Dos clases
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def obtener_datos_persona(self):
        print(f'El nombre de la persona es {self.nombre} y la edad es {self.edad}')
    
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
    
    def grado_persona(self):
        print(f'El grado de {self.nombre} es {self.grado}')

estudiante_1 = Estudiante('Ignacio', '27', '5to')

print(estudiante_1.nombre)
print(estudiante_1.edad)
print(estudiante_1.grado)

estudiante_1.obtener_datos_persona()
estudiante_1.grado_persona()'''

'''class Animal:
    def comer(self):
        print('Come')
    
class Mamifero(Animal):       
    def amamantar(self):
        print('Amamanta')
    
class Ave(Animal):
    def volar(self):
        print('Vuela')
        
class Murcielago(Mamifero,Ave):
    pass

murcielago_1 = Murcielago()
ave_1 = Ave()

murcielago_1.volar()
murcielago_1.comer()
murcielago_1.amamantar()

ave_1.comer()
ave_1.volar()'''

'''class Personaje:
    def __init__(self, nombre, velocidad, fuerza):
        self.nombre = nombre
        self.velocidad = velocidad
        self.fuerza = fuerza
        
    def __repr__(self):
        return f'{self.nombre} (Velocidad: {self.velocidad}, Fuerza: {self.fuerza})'
    
    def __add__(self,otro_pj):
        nuevo_personaje = self.nombre + '-' + otro_pj.nombre
        nueva_velocidad = self.velocidad + otro_pj.velocidad
        nueva_fuerza = self.fuerza + otro_pj.fuerza
        return Personaje(nuevo_personaje, nueva_velocidad, nueva_fuerza)
        
goku = Personaje('Goku',100,100)
vegeta = Personaje('Vegeta', 50, 50)
nachotelli = Personaje('Nachotelli', 150, 150)

nuevo = goku + vegeta + nachotelli
print(nuevo)'''

diccionario = {'key1': 0,'key2': 1}

diccionario['key1'] = 1
diccionario['key2'] = 2
print(diccionario.items())

for key, value in diccionario.items():
    print(key)
    print(value)