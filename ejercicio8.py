# Autor:Andersson Sanabria
# Fecha:03/05/2021
# Version:1.0
# Nombre del Proyecto:Ejercicio #8

# ----------------------Ejercicio #8-----------------------------


# Escribí un programa que le solicite al usuario ingresar una fecha formada por 
# 8 números, donde los primeros dos representan el día, los siguientes dos el mes
#  y los últimos cuatro el año (DDMMAAAA). Este dato debe guardarse en una variable
#  con tipo int (número entero). Finalmente, mostrar al usuario la fecha con el 
# formato DD / MM / AAAA.


# Ejemplo de ejecución:

# Fecha en formato DDMMAAAA: 16112017
#16 / 11 / 2017

if __name__=='__main__':
    fecha = str(input('Fecha en formato DDMMAAAA: '))
    dia = int(fecha[0:2])
    mes = int(fecha[2:4])
    anio = int(fecha[4:])
    print ('{dia}/{mes}/{anio}'.format(dia = dia,mes = mes, anio = anio))