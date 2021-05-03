# Autor:Andersson Sanabria
# Fecha:28/04/2021
# Version:1.0
# Nombre del Proyecto:Ejercicio #1

# ----------------------Ejercicio #1-----------------------------

# Escribí un programa que muestre un mensaje de bienvenida a un nuevo usuario, 
# solicitando que ingrese su nombre y a continuación se debe mostrar en pantalla el saludo.

# vamos a utlizar los siguientes comandos

# print-->Imprimir o mostrar mensajes
# input-->Solicitar datos, este espera que ingreses un valor

if __name__=='__main__':
    nombre = str(input('Bienvenido!, por favor ingrese su nombre: '))
    print('Hola {nombre}!'.format(nombre=nombre))

