# Autor:Andersson Sanabria
# Fecha:28/04/2021
# Version:1.0
# Nombre del Proyecto:Ejercicio #6

# ----------------------Ejercicio #6-----------------------------#
# Escribí un programa que solicite al usuario el ingreso de un texto y 
# almacene ese texto en una variable. A continuación, mostrar en pantalla 
# la primera letra del texto ingresado. Luego, solicitar al usuario que
# ingrese un número positivo menor a la cantidad de caracteres que tiene el 
# texto que ingresó (por ejemplo, si escribió la palabra “HOLA”, tendrá que 
# ser un número entre 0 y 4) y almacenar este número en una variable llamada indice.
# Mostrar en pantalla el carácter del texto ubicado en la posición dada por indice.

if __name__=='__main__':
    texto = str(input('Ingrese un texto: '))
    print('la primera letra es {letra}'.format(letra = texto[0]))
    indice = int(input('ingrese un número positivo menor a {caracteres}: '.format(caracteres = len(texto))))
    print('la  letra en el indice {indice} es: {letra}'.format(indice = indice, letra = texto[indice]))

