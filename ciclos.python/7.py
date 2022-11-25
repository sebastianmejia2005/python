numero = int(input("Ingrese un número: "))

suma = 0

for i in range(1,numero,1):
    print(i)
    suma += i
    if suma > numero:
        break
print("Suma: ",suma)