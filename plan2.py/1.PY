#Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.
a = int(input("escriba un nro: "))
b = int(input("escriba un nro: "))

def max(a,b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "iguales"

print(max(a,b))