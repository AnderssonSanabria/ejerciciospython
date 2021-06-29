#Hacer un programa en lenguaje Python que lea el nombre y el peso de un estudiante de un colegio
#  e imprima un mensaje informando su nombre y rango de peso con base en la siguiente tabla:
#Estudiantes de menos de 40 kg.
#Estudiantes entre 40 y 50 kg.
#Estudiantes de más de 50 kg y menos de 60 kg.
#Estudiantes de más o igual a 60 kg.

estudiante = str(input('Ingrese el nombre del estudiante: '))
peso = float(input('Ingrese el peso del estudiante en Kg: '))
rango_de_peso = ''

if peso < 40:
    rango_de_peso = 'menos de 40 kg'
elif peso >= 40 and peso <= 50:
    rango_de_peso = 'entre 40 y 50 kg'
elif peso > 50 and peso < 60:
    rango_de_peso = 'más de 50 kg y menos de 60 kg'
else:
    rango_de_peso = 'más o igual a 60 kg'

print('el rango de peso de {} es de {}'.format(estudiante, rango_de_peso))