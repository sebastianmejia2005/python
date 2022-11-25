import math

a = int(input("Digite el primer valor"))
b = int(input("Digite el segundo valor"))
c = int(input("Digite el tercer valor"))

if ((b**2) - 4 * a * c) < 0:
    ("No se puede solucionar") 
else:
    x1=(-b+math.sqrt(b**2-(4*a*c)))/(2*a) 
    x2=(-b-math.sqrt(b**2-(4*a*c)))/(2*a)
                                            
print(x1)
print(x2)