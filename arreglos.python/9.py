import random

columnas = round(random.randint(2,5))
lista = [[round(random.random()*100) for col in range(columnas)] for fil in range(random.randint(2,5))]

print(lista)
