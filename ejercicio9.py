# Autor:Andersson Sanabria
# Fecha:15/04/2021
# Version:1.0
# Nombre del Proyecto:Ejercicio #9

# ----------------------Ejercicio #9-----------------------------

# Escribir un programa que solicite ingresar su nombre y edad, luego los almacene,
#  y los muestre en pantalla, mediante la funcion f-string, luego utilizar un condicional
#  if para saber si es mayor de edad.

if __name__=='__main__':
    nombre = str(input('Ingrese su nombre: '))
    edad = int(input('Ingrese su edad: '))
    print(f"Hola, my nombre es {nombre} y mi edad es {edad}")
    if(edad>=18):
        print(f'{nombre} Es mayor de edad')
    else:
        print(f'{nombre} No es mayor de edad')