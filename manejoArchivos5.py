archivo=open("/mnt/c/Users/ander/proyectos/mintic/prueba.txt")
# leer sin espacios en blanco desde el punto deseado
for linea in archivo:
    linea=linea.rstrip()
    if  linea.find("@uct.ac.za")==-1:
        continue
    print(linea)
archivo=open("/mnt/c/Users/ander/proyectos/mintic/prueba.txt")
# leer sin espacios en blanco desde el punto deseado
for linea in archivo:
    linea=linea.rstrip()
    if  linea.find("@uct.ac.za")==-1:
        continue
    print(linea)