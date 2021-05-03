# Autor:Andersson Sanabria
# Fecha:28/04/2021
# Version:1.0
# Nombre del Proyecto:Ejercicio #2

# ----------------------Ejercicio #2-----------------------------
# Escribí un programa que solicite al usuario dos números y los almacene en dos variables.
# En otra variable, almacená el resultado de la suma de esos dos números y luego mostrá 
# ese resultado en pantalla.
# A continuación, el programa debe solicitar al usuario que ingrese un tercer número, 
# el cual se debe almacenar en una nueva variable. Por último, mostrá en pantalla el
#  resultado de la multiplicación de este nuevo número por el resultado de la suma anterior.

if __name__=='__main__':
    variable_1 = int(input('Ingrese el primer numero: '))
    variable_2 = int(input('Ingrese el segundo numero: '))
    suma = variable_1 + variable_2
    variable_3 = int(input('Ingrese el tercer numero: '))

    print('el resultado de la suma  del primer numero mas el segundo numero, por el tercer numero es: {multiplicacion}!'.format(multiplicacion=suma *variable_3))
