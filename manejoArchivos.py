# leer usando la función read
# imprimir fracciones del archivo
archivo=open("/mnt/c/Users/ander/proyectos/mintic/prueba.txt")
# cuenta los caracteres del archivo
caracteres= archivo.read()
print("El archivo tiene: ", len(caracteres), "caracteres")
print(caracteres[:200])