import random

tamaño = random.randint(10,25)
lista = [round(random.random()*100) for i in range(random.randint(10,25))] #Código más corto - eficiente - Comprensión
print(lista,' tamaño:', len(lista))

suma = 0
promedio = 0
