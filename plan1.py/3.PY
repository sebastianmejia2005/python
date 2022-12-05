'''Definir un histograma procedimiento() que tome una lista de números enteros e imprima un
histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
****
*********
******* '''

import random

list = [random.randint(1,10) for i in range(4)]
print(list)

def histograma(list):
    for i in list:
        sum = 0
        cont = "* "
        for j in range (1,i):
            if sum <= i:
                sum -= 1
                cont += "* "
        print(cont)
    
histograma(list)