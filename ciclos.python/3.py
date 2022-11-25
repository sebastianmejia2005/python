numero = int(input("Ingrese un nùmero: "))

sumaDivisores = 0

for i in range(1,numero,1):
    if numero % i == 0:
        sumaDivisores += i # Empieza en 0 y se van sumando los divisores

if sumaDivisores == numero:
    print("El número ",numero," es perfecto")
else:
    print("El número ",numero," no es perfecto")
 