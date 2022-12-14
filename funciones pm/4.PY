#Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n

a = input('escriba una letra: ')
b = int(input('escriba un numero: '))

def n_caracter(a,b):
    v = ""
    for i in range(b):
        v += a
    return v
    
print(n_caracter(a,b))