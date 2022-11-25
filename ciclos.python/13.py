numero = int(input("Ingrese un número: "))

inverso = 0

while numero > 0:
    residuo = numero % 10
    inverso = (inverso * 10) + residuo
    #break
    numero //= 10

print('El inverso del número ingresado es: ', inverso)