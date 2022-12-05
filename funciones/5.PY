'''Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1
miembro en común o devuelva False de lo contrario.'''

import random

list1 = [random.randint(1,10) for i in range(4)]
print(list1)
list2 = [random.randint(1,10) for i in range(4)]
print(list2)

def superpos(list1,list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False
    
print(superpos(list1,list2))