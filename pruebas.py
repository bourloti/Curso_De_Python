int, float, str, bool

lista = [1,'hola',3,True,5.0]
lista2 = [23,54,1234,65,34,65,34]

tupla = (1, 'nacho', False, 10.5)

diccionario = {'nombre': ['nacho','lean','santi'], 
               'apellido': ['bourlot','bonato','cachencho'], 
               'clave3': 14}

conjuntos = {1,2,3.5, False}

'''lista.append('nachoetlli10')
valor_de_lista = lista[1]
print(lista.index(5.0))
lista2.sort()
print(lista2)
lista2.insert(2,4.6)
lista2.extend([23,43,654,3])
print(lista2)
print(dir(lista))
print(valor_de_lista)
print(lista)'''

'''valor_clave_1 = diccionario['clave1']
print(valor_clave_1)
'''



while True:
    try:
        nombre = input('Colocar nombre para buscar apellido: ')
        indice = diccionario['nombre'].index(nombre)
        apellido = diccionario['apellido'][indice]
        print(f'El nombre es {nombre.capitalize()} y el apellido {apellido.capitalize()}')
    except:
        print('El nombre no existe')



