import random

tamaño = random.randint(10,25)
lista = [round(random.random()*100) for i in range(random.randint(10,25))] #Código más corto - eficiente
print('Lista:',lista)

sumapar = 0
pares = []