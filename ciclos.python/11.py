dividendo = int(input("Ingrese el primer número (dividendo): "))
divisor = int(input("Ingrese el segundo número (divisor): "))

cociente = 0

while dividendo >= divisor:
    dividendo -= divisor
    cociente += 1

print("El residuo es: ", dividendo)
print("El cociente es: ",cociente)