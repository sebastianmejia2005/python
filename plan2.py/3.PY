#Escribir una funcion sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista.
import random

list = [random.randint(1,10) for i in range(5)]
print(list)

def sum(list):
    suma = 0
    for i in list:
        suma += i
    return suma
    
def multip(list):
    prod = 1
    for i in list:
        prod *= i
    return prod
    
print('la suma de los digitos es: ',sum(list))
print('la multiplicacion de los digitos es: ',multip(list))