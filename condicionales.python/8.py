num1 = int(input("Digite el primer número"))
num2 = int(input("Digite el segundo número"))
num3 = int(input("Digite el tercer número"))

numeroMenor = min(num1,num2,num3)
numeroMayor = max(num1,num2,num3)

numeroMedio = (num1 + num2 + num3) - numeroMayor - numeroMenor

print("El número del medio es: ",numeroMedio)