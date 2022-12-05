#Definir una función inversa() que calcule la inversión de una cadena.

nombre = input('Escriba una palabra: ')

def invert(n):
    return n[::-1]

print(invert(nombre))