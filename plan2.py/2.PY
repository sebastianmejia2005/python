#Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.

a = int(input("escriba un nro: "))
b = int(input("escriba un nro: "))
c = int(input("escriba un nro: "))

def max(a,b,c):
    if a < b:
        if a > c:
            return a
    if b > c:
        if b > a:
            return b
    if c > a:
        if c > b:
            return c
    

print(max(a,b,c))