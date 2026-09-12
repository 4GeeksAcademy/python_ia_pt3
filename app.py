import random

# tips de datos:

#booleano: true, false -> True False
#number: int(entero) float(decimales)
#string: str (cadenas de texto)
#null y undefined -> None (valor nulo)
#array -> listas list []
#objetos -> directorios dir  {}
# tuplas -> () listas ordenadas inmutables


#variables
# let edad = 26
# const nombre = "astrid"

edad = 26
NOMBRE = "Astrid"
esProfe = True 

print(NOMBRE, edad)  #console.log()

#let array = [1, 2, 3 ,4]

lista = [1, 2, 3 ,4 ]

print(lista)

#array.push(6)
lista.append(6)
print(lista)

#length __ len 
print(len(lista))

tupla=("lunes", "miercoles", "viernes")

print(f"el primer dia de clase es: {tupla[0]}")
# f-strings interpolar variables `` ${} que usabamos en js 


#let objeto ={nombre: "Juan", edad: 26, "ciudad de nacimiento": "Bogota"}

dict = {
"nombre": "Juan",
"edad": 26,
"ciuadad de nacimiento": "Bogota" }

print(dict["nombre"])

#funciones

# function saludar(){
# console.log("hola alumnos")
#}

# saludar()

def saludar(nombre):
    print(f"hola {nombre}")

saludar("miguel")
saludar("jhoan")




def sumar (a, b):
    resultado= a+b
    return resultado
total= sumar(5,3)
print(f"la suma de 5 y 3 es: {total}")


x=8
#if(x>10){
# console.log("x es mayor que 10")
#}
#else if (x===10){console.log("x es igual a 10")}
#else{console.log("x es menor a 10")}

if x>10:
    print("x es mayor que 10" )
elif x==10:
    print("x es igual a 10" )
else:
    print("x es menor a 10" )

#bucles y funcion range()

# for (let i=0; i<10; i++){
#     console.log(i)
# })




for i in range(10):
    print(i)

#range      (start, stop, step)
for i in range(10, -1, -1):
    print(i)
    pass 

for i in range(0, 11, 2):
    print(i)
    pass


contador=5
print(f"contador inicializado {contador}")
while contador > 0:
    print(contador)
    contador -= 1
print(f"contador finalizado {contador}")


## multiples asignaciones en una sola linea 
a, b, c = 1, 2 , 3 

print(b)

## genear un valor ramdon 
numero_aleatorio= random.randint(1, 10)
print(f"numero aleatorio: {numero_aleatorio}")

