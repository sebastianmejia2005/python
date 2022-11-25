numero = float(input("Digite un número de 0 a 9.999 para saber cuántas cifras tiene: "))

if numero < 0:
    print("Número inválido")
elif numero < 100:
    print("Su número tiene dos cífras")
elif numero < 1000:
    print("Su número tiene tres cífras")
elif numero < 10000:
    print("Su número tiene cuatro cífras")
else:
    print("Su número excede los límites")