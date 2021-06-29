contador=0
nombre=input("Ingrese la palabra a buscar: ")
archivo=open("/mnt/c/Users/ander/proyectos/mintic/prueba.txt")
# leer desde una posicion o parte deseada
for linea in archivo:
    if linea.startswith(nombre):
        contador=contador+1
        #print(linea)
print(contador)