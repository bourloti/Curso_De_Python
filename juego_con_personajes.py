import pandas as pd

class Personaje:
    def __init__(self, nombre, velocidad, fuerza):
        self.nombre = nombre
        self.velocidad = velocidad
        self.fuerza = fuerza
    
    def __repr__(self):
        return f'({self.nombre}, {self.velocidad}, {self.fuerza})'
    
    def __add__(self, otro_pj):
        nuevo_nombre = self.nombre[:3] + otro_pj.nombre[-3:]
        nueva_velocidad = self.velocidad + otro_pj.velocidad
        nueva_fuerza = self.fuerza + otro_pj.fuerza
        return Personaje(nuevo_nombre, nueva_velocidad, nueva_fuerza)

df = pd.read_csv('Curso_De_Python\\juego_de_personajes.csv')
listaPersonajes = list(df.itertuples(index=False, name=None))
print(df)
print(listaPersonajes)

def Mostrar_personajes():
    df = pd.read_csv('Curso_De_Python\\juego_de_personajes.csv')
    df_nuevo = df.dropna()
    df_nuevo.to_csv('Curso_De_Python\\juego_de_personajes.csv', index=False)
    
    print(df_nuevo)

def Crear_persoajes():
        personaje = input('Colocar nombre de personaje a agregar: ')
        velocidad = int(input('Colocar velocidad (0 a 100): '))
        fuerza = int(input('Colocar fuerza (0 a 100): '))
        
        #personaje_objeto = Personaje(personaje, velocidad, fuerza)
        #listaPersonajes.append(personaje_objeto)
        #print(listaPersonajes)

        agregar_personaje = {'nombre': [personaje], 'velocidad': [velocidad], 'fuerza': [fuerza]}

        df_nuevo = pd.DataFrame(agregar_personaje)
        print(df_nuevo)
        df_nuevo.to_csv('Curso_De_Python\\juego_de_personajes.csv', mode= 'a', index=False, header=False)
        #return listaPersonajes
    
def Fusionar_personajes():
    df = pd.read_csv('Curso_De_Python\\juego_de_personajes.csv')
    print(df)
    
    personaje1 = int(input('Que personajes quieres fusionar?: '))
    personaje2 = int(input('Que personajes quieres fusionar?: '))
    
    personaje_objeto_1 = Personaje(df.loc[personaje1,'nombre'], df.loc[personaje1,'velocidad'], df.loc[personaje1,'fuerza'])
    personaje_objeto_2 = Personaje(df.loc[personaje2,'nombre'], df.loc[personaje2,'velocidad'], df.loc[personaje2,'fuerza'])

    fusion = personaje_objeto_1 + personaje_objeto_2

    print(fusion)

while True:
    print('''Elegir opcion para comenzar:
    1- Crear personaje
    2- Fusionar personajes
    3- Mostrar personajes''')

    opcion = input('Elegir: ')

    if opcion == '1':
        Crear_persoajes()
    if opcion == '2':
        if len(listaPersonajes) < 2:
            print('No hay suficientes personajes para fusionar')
        else:
            Fusionar_personajes()        
    if opcion == '3':
        Mostrar_personajes()
    
        

