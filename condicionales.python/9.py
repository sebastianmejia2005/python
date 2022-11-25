numero = int(input("Digite un número de 1 a 365 para saber qué mes y día del año es"))

if numero < 0:
    print("número erroneo")
elif numero < 31:
    print("es",numero,"de enero")
elif numero < 60:
    print("es",numero - 31,"de febrero") 
elif numero < 91:
    print("es",numero - 59,"de marzo") 
elif numero < 121:
    print("es",numero - 90,"de abril") 
elif numero < 152:
    print("es",numero - 120,"de mayo") 
elif numero < 182:
    print("es",numero - 151,"de junio")
elif numero < 213:
    print("es",numero - 181,"de julio")
elif numero < 244:
    print("es",numero - 212,"de agosto")
elif numero < 274:
    print("es",numero - 243,"de septiembre")
elif numero < 305:
    print("es",numero - 273,"de octubre") 
elif numero < 335:
    print("es",numero - 304,"de noviembre")
elif numero < 366:
    print("es",numero - 334,"de diciembre")
elif numero > 365:
    print("El número excede los límites")