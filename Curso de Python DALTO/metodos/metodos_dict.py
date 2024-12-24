diccionario = {
    "nombre" : {'lucas': 43, 'fsdf':54},
    "apellido" : 'dalto',
    "subs" : 1000000
}

#nos devuelve un objeto dict_item
claves = diccionario.keys()

#obteniendo un elemento con get() (si no encuentra nada el programa continùa)
valor_de_kasdks = diccionario["nombre"].get('lucas')
print(valor_de_kasdks)
print("hola papa, el programa continua")

#eliminando todo del diccionario
#diccionario.clear()

#eliminando un elemento del diccionario
diccionario.pop("subs")

#obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)

diccionario = {'a': 1, 'b': 2, 'c': 3}
for clave in diccionario:
    print(clave)  # Imprime 'a', 'b', 'c'

dicc = list(diccionario.items())
print(dicc)
