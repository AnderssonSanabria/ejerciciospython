# Autor:Andersson Sanabria
# Fecha:28/04/2021
# Version:1.0
# Nombre del Proyecto:Ejercicio #5
# Correo:tucorreo@hotmail.com

# ----------------------Ejercicio #5-----------------------------#
# Escribí un programa que solicite al usuario el ingreso de dos palabras, 
# las cuales se guardarán en dos variables distintas. A continuación, 
# almacená en una variable la concatenación de la primera palabra, más un espacio, 
# más la segunda palabra. Mostrá este resultado en pantalla.

if __name__=='__main__':
    palabra_1 = str(input('Ingrese la primera palabra: '))
    palabra_2 = str(input('Ingrese la segunda palabra: '))
    concatenacion = palabra_1 + ' ' + palabra_2
    print(concatenacion)
