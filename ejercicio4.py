# Autor:andersson Sanabria
# Fecha:28/04/2021
# Version:1.0
# Nombre del Proyecto:Ejercicio #4

# ----------------------Ejercicio #4-----------------------------#
# Escribí un programa que solicite al usuario un número y le reste el 15%, 
# almacenando todo en una única variable. A continuación, mostrar el resultado final
# en pantalla.

# Ejemplo de ejecución:
# Ingresá un número: 260
# Descontando el 15% queda: 221.0

if __name__=='__main__':
    variable = int(input('Ingrese un numero: '))
    variable = variable - variable*0.15
    print('El 85% del valor ingresado es: {variable}'.format(variable = variable))
