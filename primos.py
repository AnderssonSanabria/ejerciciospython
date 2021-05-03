def primos(n):
    es_prim=True
    if n % 1 == 0:
        for values in range(2,n-1):
            if n % values==0:
               es_prim=False
    return es_prim

         
            
if __name__=='__main__':
    n=int(input('escribe un numero: '))
    primo=primos(n)

    if primo==True:
        print('El numero {} es primo'.format(n))
    else:
        print('El numero {} no es primo'.format(n))