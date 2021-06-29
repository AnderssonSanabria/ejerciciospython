import sys
import os
menu = '''
**************Menu**************
1. Numero mayor que cero
2. Par o impar
3. Subsiio de transporte
4. Notas Estudiante
5. Pico y placa
6. Producto
7. Ecuacion de segundo grado
8. Bolita
9. cuadrado - cubo raiz
10. Dias de la semana
11. Salir 
'''
print(menu)
opcion = int(input('Elija una opcion: '))
os.system('clear')
if opcion == 1:
    numero =int(input('Ingrese un numero mayor a cero: '))
    if(numero>0):
        print('el numero ingresado es mayor que cero')
elif opcion == 2:
    numero =int(input('Ingrese un numero: '))
    if((numero%2) == 0):
        print('el numero ingresado es par')
elif opcion == 3:
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
elif opcion == 4:
    pass
elif opcion == 5:
    pass
elif opcion == 6:
    pass
elif opcion == 7:
    pass
elif opcion == 8:
    pass
elif opcion == 9:
    pass
elif opcion == 10:
    pass
elif opcion == 11:
    sys.exit()
else:
    print('La opcion ingresada no es valida')