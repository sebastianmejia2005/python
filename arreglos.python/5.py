import random

tamaño = random.randint(10,25)
lista = [round(random.random()*100) for i in range(random.randint(10,25))] #Código más corto - eficiente
print('lista: ',lista)

for i in range(len(lista) - 1):
    for j in range(len(lista) - 1 - i):
