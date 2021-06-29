if __name__ == '__main__':
    contador_dias = 0
    contador_min = 0
    contador_max = 0
    contador_ambos = 0
    media_max = 0
    media_min = 0
    max_total=0
    min_total=0
    dias_error = 0
    inicio=True
    while(inicio):
        temperatura_max = int(input())
        temperatura_min = int(input())
        if(temperatura_max==0 and temperatura_min==0):
            inicio = False
            break
        contador_dias = contador_dias + 1
        if temperatura_min<5 or temperatura_max>35:
            dias_error = dias_error + 1
            if temperatura_min<5 and temperatura_max>35:
                contador_ambos = contador_ambos + 1
            else:
                if temperatura_min<5:
                    contador_min = contador_min +1
                if temperatura_max>35:
                    contador_max = contador_max +1
        else:
            max_total = max_total + temperatura_max
            min_total = min_total + temperatura_min
            
media_max=max_total/(contador_dias-dias_error)
media_min=min_total/(contador_dias-dias_error)
Porcentaje_dias_error = (dias_error*100)/contador_dias
print(contador_dias)
print(dias_error)
print(contador_min)
print(contador_max)
print(contador_ambos)
print(media_max)
print(media_min)
print(Porcentaje_dias_error)