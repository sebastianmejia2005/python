'''Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el
mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.'''

palabra = input('escriba un palindromo: ')

def es_palindromo(n):
    palindromo = n[::-1]
    if palabra = palindromo:
        return True
    else:
        return False

print(es_palindromo(palabra))