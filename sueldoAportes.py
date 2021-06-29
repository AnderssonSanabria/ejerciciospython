# Hacer un programa que permita leer el nombre de un empleado y salario.
# Calcular el subsidio de transporte, aporte, salud, aporte pensión y total a pagar. 
# Imprimir nombre y total a pagar.
nombre =str(input('Ingrese su nombre: '))
salario =int(input('Ingrese su salario: '))
salario_minimo = 908526
subsidio_transporte = 106.454
salud= salario*0.04
pension= salario*0.04
total=0
if(salario>=(salario_minimo*2)):
    subsidio_transporte = 0
total = salario -salud - pension + subsidio_transporte
print('el total a pagar a {nombre} es: {total}'.format(nombre=nombre,total=total))

