# Un ángulo se considera agudo si es menor de 90 grados,
#  obtuso si es mayor de 90 grados y recto si es igual a 90 grados.
#  Utilizando esta información, escribir un programa que acepte un ángulo en grados
#  y visualice el tipo de ángulo correspondiente a los grados introducidos.

angulo = float(input('Ingrese el angulo en grados: '))
tipo_angulo = ''

if angulo < 90:
    tipo_angulo = 'agudo'
elif angulo == 90:
    tipo_angulo = 'recto'
else:
    tipo_angulo = 'obtuso'

print('el angulo de {}° es {}'.format(angulo, tipo_angulo))  