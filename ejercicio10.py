# Autor:Andersson Sanabria
# Fecha:03/04/2021
# Version:1.0
# Nombre del Proyecto:Ejercicio #10

# ----------------------Ejercicio #10-----------------------------

# Escribir un programa que solicite ingresar cuanto dinero tiene en su cartera,
# el precio total de los productos que va a comprar y le diga si le alacanza o no

if __name__=='__main__':
    dinero = float(input('Cuanto dinero tiene en su cartera: '))
    precio_productos =  float(input('Cual es el precio de los productos: '))
    
    if(dinero>=precio_productos):
        print('El dinero si le alcanza')
    else:
        print(f'El dinero no le alcanza, debe tener mas de $ {precio_productos}')