
def calculoValorHoras(horas,valor_hora,horas_semana):
    values= {'total_h_normales':0,'total_extras':0,'valor_bruto':0}
    
    if horas <= horas_semana:
        values['total_h_normales'] = (horas)*(valor_hora)
    elif horas>horas_semana:
        values['total_h_normales'] =valor_hora * horas_semana
        values['total_extras'] = (horas - horas_semana)*(1.5*valor_hora)
    values['valor_bruto'] = values['total_h_normales'] + values['total_extras'] 
    return values

def calculoDescuentosProvisiones(sueldo,porcentaje):
    resultado = sueldo * porcentaje
    return resultado

if __name__ =='__main__':
    nombre = input('Ingrese su nombre')
    horas_trabajadas = int(input('Ingrese el numero de horas trabajadas en la semana'))
    valor_hora_trabajada = int(input('Ingrese el valor por hora trabajada'))
    horas_semana = 40
    #calclo horas
    horas = calculoValorHoras(horas_trabajadas,valor_hora_trabajada,horas_semana)
    sueldo_bruto = horas['valor_bruto']
    #calculo descuentos
    descuento_parafiscales = calculoDescuentosProvisiones(sueldo_bruto,0.09)
    descuento_salud = calculoDescuentosProvisiones(sueldo_bruto,0.04)
    descuento_pension = calculoDescuentosProvisiones(sueldo_bruto,0.04)
    total_descuentos = descuento_parafiscales + descuento_salud + descuento_pension

    sueldo_neto = sueldo_bruto - total_descuentos
    #calculo provisiones
    provision_prima = calculoDescuentosProvisiones(sueldo_bruto,0.0833)
    provision_cesantias = calculoDescuentosProvisiones(sueldo_bruto,0.0833)
    provision_i_cesantias = calculoDescuentosProvisiones(sueldo_bruto,0.01)
    provision_vaciaciones = calculoDescuentosProvisiones(sueldo_bruto,0.0417)
    for word in horas:
        print(horas[word])
    print(descuento_parafiscales)
    print(descuento_salud)
    print(descuento_pension)
    print(total_descuentos)
    print(sueldo_neto)
    print(provision_prima)
    print(provision_cesantias)
    print(provision_i_cesantias)
    print(provision_vaciaciones)

