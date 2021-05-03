# Autor:Andersson Sanabria
# Fecha:28/04/2021
# Version:1.0
# Nombre del Proyecto:Ejercicio #3

# ----------------------Ejercicio #3-----------------------------
# Escribí un programa que solicite al usuario ingresar tres números 
# para luego mostrarle el promedio de los tres.
if __name__=='__main__':
    variable_1 = int(input('Ingrese el primer numero: '))
    variable_2 = int(input('Ingrese el segundo numero: '))
    variable_3 = int(input('Ingrese el segundo numero: '))
    promedio = (variable_1 + variable_2 + variable_3)/3
    print('El promedio es: {promedio}'.format(promedio = promedio))