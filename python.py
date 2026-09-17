#casting de tipos de datos 

# int() 
# float()
# str()
# bool()
# list() -> (map / filter)
# tuple()
# dict()

precio_texto = "49,99"
print( "texto original:", precio_texto, type(precio_texto))


precio_decimal= float(precio_texto.replace(",", "."))

print( "texto covertido a float:", precio_decimal, type(precio_decimal))


precio_entero= int(precio_decimal)
print( "texto convertido a entero:", precio_entero, type(precio_entero))


#funciones

def calcular_area_rectangulo (base, altura):
    area= base * altura
    return area 

resultado_area = calcular_area_rectangulo(5,10)
print("el area del rectangulo es:", resultado_area)

#alcance 

impuesto_global= 0.15

def calculr_precio_final(precio_base):
    descuento_local= 5.0

    precio_con_descuento= precio_base - descuento_local
    precio_final= precio_con_descuento + (precio_con_descuento * impuesto_global)

    return precio_final

print("precio final con impuestos:", calculr_precio_final(100))
# print(descuento_local) esto da ERROR no existe fuera de la funcion 
print(impuesto_global)



# funciones anidadas:

#primera funcion suma 5 dolares de envio a un precio base

def agregar_envio(precio):
    return precio + 5

#segunda funcion agrega 10% de impuesto al total recibido

def agregar_impuestos(precio_con_envio):
    return precio_con_envio * 1.10

costo_total= agregar_impuestos(agregar_envio(50))

print("el costo total con envio e impuestos es: ", costo_total)




#funciones lambda (funciones de una linea)

#ejemplo 1
elevar_al_cuadrado= lambda x: x**2
print("cuadrado de 4: ", elevar_al_cuadrado(4))

#ejemplo 2

numeros= [1,2,3,4,5]

cuadrados= list(map(lambda x: x**2, numeros))

print(cuadrados)



#ejemplo 3

nombres= ["ana", "luis", "maria"]

nombres_mayuscula= list(map(lambda palabra: palabra.upper(), nombres))

print(nombres_mayuscula)