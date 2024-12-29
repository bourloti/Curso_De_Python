
#creando una lista (se pueden modificar)
lista = ["Lucas Dalto","Soy Dalto",True,1.85, "Soy Dalto"]

#creando una tupla (no pueden modificar)
tupla = ("Lucas Dalto","Soy Dalto",True,1.85, "Soy Dalto")

#esto es vàlido
#lista[3] = "Maquinola"

#esto no
#tupla[3] = "Maquinola"


#creando un conjunto (set) (no se accede a elementos por ìndice, no almacena datos duplicados)
conjunto = {"Lucas Dalto","Soy Dalto",True,1.85, "Soy Dalto"}

#print(conjunto[3]) -> no puede acceder al elemento


#creando un diccionario (dict) (la estructura es key : value y separamos con comas)
diccionario = {
    'nombre' : "Lucas Dalto",
    'canal' : "Soy Dalto",
    'esta_emocionado' : True,
    'altura' : 1.85,
    'dato_duplicado' : "Soy Dalto"
}

print(list(diccionario.values()))
print(diccionario)

for i in diccionario.values():
    print(i)
    if i == "canal":
        print(diccionario['canal'])

lista1 = ['nacho', 'lean', 'santi']
lista2 = [23, 34, 54]

condicion = ''

while condicion != 'salir':
    lista1.append(input("decime nombre: "))
    lista2.append(int(input('decime edad: ')))
    condicion = input("decime condicion: ")

nombre = input("que nombre buscar: ")
if nombre in lista1:
    indice_de_valor = lista1.index(nombre)
    edad_de_persona = lista2[indice_de_valor]
    print(edad_de_persona)
else:
    print('nombre no existe')



