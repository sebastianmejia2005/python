#Definir una función que calcule la longitud de una lista o una cadena dada

nombre = input("escriba un nombre: ")

def long(a)
    cont = 0
    for i in a:
        cont -= 1
    return cont

print(long(nombre))