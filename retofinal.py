import os
def verListado():
    print('Listado de beneficiarios')
    agenda = open('agenda.txt', "r")
    for linea in agenda:
        linea=linea.rstrip()
        print(linea)
    agenda.close()
def verListadoFiltrado():
    agenda = open('agenda.txt', "r")
    listado = []
    print('Digite la letra por la que empiezan los beneficiarios:')
    letra_inicial = input()
    for linea in agenda:
        linea=linea.rstrip()
        listado.append(linea)
    print('Listado filtrado de beneficiarios:')
    for linea in listado:
        if letra_inicial.lower() == linea[0].lower():
            indice = listado.index(linea)
            print(listado[indice])
            print(listado[indice+1])
            print(listado[indice+2])
    agenda.close()
def agregarBeneficiario():
    print('Digite la información del beneficiario a agregar:')
    nombre = input()
    cedula = input()
    celular = input()
    agenda = open('agenda.txt', "a")
    agenda.write(nombre)
    agenda.write('\n')
    agenda.write(cedula)
    agenda.write('\n')
    agenda.write(celular)
    agenda.write('\n')
    agenda.close()
    
    print('El beneficiario ha sido agregado')
def buscarBeneficiario():
    print('Digite el nombre y apellido del beneficiario a buscar:')
    beneficiario_a_buscar = input()
    agenda = open('agenda.txt', "r")
    listado = []
    for linea in agenda:
        linea=linea.rstrip()
        listado.append(linea)
    for linea in listado:
        if beneficiario_a_buscar.lower() == linea.lower():
            indice = listado.index(linea)
            print(listado[indice])
            print(listado[indice+1])
            print(listado[indice+2])
    agenda.close()
def borrarBeneficiario():
    print('Digite la cedula del beneficiario a borrar:')
    benefificario_a_borrar = input()
    agenda = open('agenda.txt', "r")
    listado = []
    for linea in agenda:
        linea=linea.rstrip()
        listado.append(linea)
    for linea in listado:
        if benefificario_a_borrar.lower() == linea.lower():
            indice = listado.index(linea)
            listado.remove(listado[indice-1])
            listado.remove(listado[indice-1])
            listado.remove(listado[indice-1])
    agenda.close()
    agenda = open('agenda.txt', "w")
    agenda.close()
    for linea in listado:
        agenda = open('agenda.txt', "a")
        agenda.write(linea)
        agenda.write('\n')
        agenda.close()
    
    print('El usuario ha sido eliminado del listado') 
def salir():
    print('Hasta pronto')

if __name__ == '__main__':
    while True:
        print('Menu Principal')
        print('1. Ver listado')
        print('2. Ver listado filtrado')
        print('3. Agregar beneficiario')
        print('4. Buscar beneficiario')
        print('5. Borrar beneficiario')
        print('6. Salir')
        agenda = open('agenda.txt', mode='a') 
        agenda.close()

        seleccion = int(input())
        if seleccion == 1:
            verListado()
        elif seleccion == 2:
            verListadoFiltrado()
        elif seleccion == 3:
            agregarBeneficiario()
        elif seleccion == 4:
            buscarBeneficiario()
        elif seleccion == 5:
            borrarBeneficiario()
        else:
            salir()
            break
