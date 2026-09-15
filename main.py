#listas [ ]

mi_lista_vacia =[]

frutas = ["manzana", "banana", "cereza"]
datos_mixtos= [1, "hola", 3.1416, True]

print(len(frutas))
print(frutas[0])
print(frutas[-1])

#Actualizar (modificar) un elemnto de mi lista

frutas[1]= "lima"
print(frutas)

frutas.append("mango")
print(frutas)

frutas.insert(1, "sandia")
print(frutas)


#eliminando elementos (remove, pop, del)
letras = ["a", "b", "c", "b", "d"]

letras.remove("b")
print(letras)

#pop elimia el elemento de un indice especifico, si no se asa indice, borra el ultimo. 
eliminado = letras.pop(2)
print(eliminado)
print(letras)

del letras[0]
print(letras)


#recorrer las listas usando range() o len()


tecnologias= ["python", "Javascript", "SQL"]


#iterando sobre el elemento 
for tech in tecnologias:
    print (tech)


#iterando sobre usando la posicion (indice)
for i in range(len(tecnologias)):
    print(f"indice {i}: {tecnologias[i]}")



#declaracion de diccionario

estudiante= {
    "nombre": "Ana",
    "edad": 36,
    "carrera": "Ingenieria",
    "activo": True
}
print(estudiante["nombre"])

#añadir dato nuevo

estudiante["promedio"]= 9.5
print(estudiante
)

#modificar un dato existente
estudiante["edad"]= 37
print(estudiante)

#eliminar datos

del estudiante["activo"]
print(estudiante)

edad_eliminada= estudiante.pop("edad")
print(edad_eliminada)
print(estudiante)

#recorriendo los dic y metodos rincipales

# .keys()  extrae las claves (propiedades)
# .values() extrae solo los valores 
# .items() extrae todo

for clave, valor in estudiante.items():
    print(f"{clave}: {valor}")

print("valores:", list(estudiante.values()))


## algoritmos de ordenamiento 

#ordenamiento de burbuja (bubble sort)

def bubble_sort(lista):
    n = len(lista) 
    for i in range(n):
        for j in range (0, n - i -1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista 

numeros= [5,1,4,2]
print("bubble sorte: ", bubble_sort(numeros))



#ordenamiento por insercion (insertion sort)
def insertion_sort(lista):
    for i in range(1, len(lista)):
        clave= lista[i]
        j= i -1
        while j >=0 and lista[j] >clave:
            lista[j+1] = lista[j]
            j-=1
        lista[j+1]= clave

    return lista

numero= [4,2,1,3]
print("insertion sort: ", insertion_sort(numero))


# algoritmos de busqueda 

def busqueda_binaria(lista_ordenada, objetivo):
    izquierda= 0 
    derecha =len(lista_ordenada) -1

    while izquierda <= derecha:
        medio= (izquierda + derecha)// 2

        #caso 1 : lo encontre justo en el medio
        if lista_ordenada[medio]==objetivo:
            return medio

        #caso 2: lo que busco es mayor, esta en la mitad derecha
        elif lista_ordenada[medio]<objetivo:
            izquierda= medio +1 

        #caso 3: lo que busco es menor, esta en la mitad izquierda
        else: 
           derecha= medio -1
    return -1

datos= [ 2,5,8,12,20]
resultado= busqueda_binaria(datos, 12)
print(f"el elemnto encontradao en el indice: {resultado}")



