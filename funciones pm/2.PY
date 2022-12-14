#Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

c = input('escriba una letra: ')

def vocal(c):
    lista = ['a','e','i','o','u','A','E','I','O','U']
    for i in lista:
        if c == i:
            return True
    return False

print(vocal(c))