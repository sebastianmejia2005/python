#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
#pregunte al usuario por la contraseña e imprima por pantalla si la contraseña 
#introducida por el usuario coincide con la guardada en la variable.

contraseña = 'python'

while True:

    usuario = input('Ingrese una contraseña: ')

    if usuario != contraseña:
        print('Contraseña incorrecta.')
    else:
        print('Contraseña correcta.')
        break