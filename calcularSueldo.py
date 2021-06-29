nombre=str(input('Ingrese el nombre del empleado: '))
hora=float(input('Ingrese el valor de la hora: '))
n=float(input('Ingrese el numero de horas trabajadas: '))
total_sueldo=(n*hora)
descuento=total_sueldo*0.04
total_sueldo=total_sueldo-descuento
print('El sueldo total del empleado es {total_sueldo}'.format(total_sueldo=total_sueldo))