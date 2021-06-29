#Hacer un programa en lenguaje python para una tienda que ofrecerá descuentos a un cliente.
#  Se considerará el nombre del producto, el precio y unidades adquiridas por el cliente, quien,
#  en el momento de pagar su compra, en la caja, sacará una bolita. Si el color de la bolita es negro,
#  el descuento será del 40%, si el color de la bolita es rojo, el descuento será del 30%, 
# si el color de la bolita es verde, el descuento será del 60%, si el color de la bolita es azul,
#  el descuento será del 50%, si el color de la bolita es amarillo, el descuento será del 20%,
#  si el color de la bolita es blanco, no tendrá descuento. Imprimir el nombre del cliente,
#  nombre del producto, el color de la bolita, el descuento y el total a pagar.

cliente = str(input('Ingrese el nombre del cliente: '))
producto = str(input('Ingrese el nombre del producto: '))
precio = float(input('Ingrese el precio del producto: '))
cantidad = int(input('Ingrese la cantidad de productos: '))
color_bolita = str(input('Ingrese el color de de la bolita que saco el cliente: '))
descuento_bolita_negra = 0.40
descuento_bolita_roja = 0.30
descuento_bolita_verde = 0.60
descuento_bolita_azul = 0.50
descuento_bolita_amarilla = 0.20
descuento_bolita_blanca = 0
descuento = 0
subtotal = 0
total_a_pagar = 0

subtotal = (precio * cantidad)

if color_bolita == 'negra':
    descuento = descuento_bolita_negra
elif color_bolita == 'roja':
    descuento = descuento_bolita_roja
elif color_bolita == 'verde':
    descuento = descuento_bolita_verde
elif color_bolita == 'azul':
    descuento = descuento_bolita_azul
elif color_bolita == 'amarilla':
    descuento = descuento_bolita_amarilla
elif color_bolita == 'blanca':
    descuento = descuento_bolita_blanca
else:
    print('El color ingresado es ivalido')

total_a_pagar = subtotal - (subtotal*descuento)

print('\ncliente: {}'.format(cliente))
print('producto: {}'.format(producto))
print('color de la bolita: {}'.format(color_bolita))
print('descuento : {}%'.format(descuento*100))
print('Total a pagar: ${}\n'.format(total_a_pagar))
