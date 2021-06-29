import random

if __name__ == '__main__':
    nombre = input('Ingrese su nombre: ')
    apellido = input('Ingrese su apellido: ')
    edad = int(input('Ingrese su edad en años: '))
    ingreso_familiar_smmv = float(input('Ingrese el número decimal de salarios mínimos mensuales de su ingreso familiar: '))
    puntaje_examen = random.randrange(0,100) # Resultado de la prueba aleatoria
    descuento_edad = 0 
    descuento_ingreso_familiar = 0
    descuento_puntaje_examen = 0
    descuento_total = 0
    
    if edad >= 15 and edad <= 18:
        descuento_edad = 25
    elif edad >= 19 and edad <= 21:
        descuento_edad = 15
    elif edad >= 22 and edad <= 25:
        descuento_edad = 10
    else:
        descuento_edad = 0
    
    if ingreso_familiar_smmv <=1:
        descuento_ingreso_familiar = 30
    elif ingreso_familiar_smmv >1 and ingreso_familiar_smmv <=2:
        descuento_ingreso_familiar = 20
    elif ingreso_familiar_smmv >2 and ingreso_familiar_smmv <=3:
        descuento_ingreso_familiar = 10
    elif ingreso_familiar_smmv >3 and ingreso_familiar_smmv <=4:
        descuento_ingreso_familiar = 5
    else:
        descuento_ingreso_familiar = 0

    if puntaje_examen >= 80 and puntaje_examen < 86:
        descuento_puntaje_examen = 30
    elif puntaje_examen >= 86 and puntaje_examen < 91:
        descuento_puntaje_examen = 35
    elif puntaje_examen >= 91 and puntaje_examen < 96:
        descuento_puntaje_examen = 40
    elif puntaje_examen >= 96:
        descuento_puntaje_examen = 45
    else:
        descuento_puntaje_examen = 0 
    descuento_total =descuento_edad + descuento_ingreso_familiar + descuento_puntaje_examen

    print(
        '''
        nombre:                              {nombre}
        apellido:                            {apellido}   
        descuento por edad:                  {descuento_edad}%
        descuento por ingreso familiar:      {descuento_ingreso}%
        descuento por obtener {puntaje} en el examen:{descuento_puntaje}%
        descuento total sobre la matricula:  {descuento_total}%
        '''.format(
            puntaje = puntaje_examen,
            nombre = nombre,
            apellido =apellido,
            descuento_edad = descuento_edad,
            descuento_ingreso = descuento_ingreso_familiar,
            descuento_puntaje = descuento_puntaje_examen,
            descuento_total = descuento_total,
        )
    )
    


