import random

vec = [round(random.random()*100) for i in range(10)]
print(vec)

pares = [x for x in vec if x % 2 == 0]
impares = [x for x in vec if x % 2 != 0]
print('Pares:',pares)
print('Impares:',impares)

pares2 = [x if x % 2 == 0 else 'xD' for x in vec]
print(pares2)