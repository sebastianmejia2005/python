numero = int(input("Introduzca un número: "))

contador = 0

for i in range(1,numero,1): 

    if (numero % i) == 0: 

        print(i,"es divisor de ",numero)

        contador += 1

print("el número ",numero," tiene ",contador," divisores.")