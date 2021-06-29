archivo=open("/mnt/c/Users/ander/proyectos/mintic/prueba.txt")
# leer sin espacios en blanco desde el punto deseado
for linea in archivo:
    linea=linea.rstrip()
    if not linea.startswith("From:"):
        continue
    print(linea)
