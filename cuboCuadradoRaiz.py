# Hacer un programa en lenguaje Python que lea un número y realice el siguiente proceso: 
#Si el valor es menor que cero calcular su cubo. 
#Si el valor está entre 0 y 100 calcular su cuadrado.  
#Si el valor es mayo que 100 calcular la raíz cuadrada.
#    Imprimir el número y los resultados.

numero = float(input('Ingrese un numero: '))
resultado = 0
operacion = ""
if numero < 0:
    resultado = numero**3
    operacion = 'cubo'
elif numero >= 0 and numero <= 100:
    resultado = numero**2
    operacion = 'cuadrado'
elif numero > 100:
    resultado = numero**(1/2)
    operacion = 'raiz cuadrada'

print('{} de {} es : {}'.format(operacion, numero, resultado))