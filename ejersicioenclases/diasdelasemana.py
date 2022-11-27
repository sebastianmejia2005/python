def diaSemana():
    try:
        n = int(input('Escriba numero que desee del 1 al 7: '))
        match n:
            case 1:
                print('Lunes')
            case 2:
                print('Martes')
            case 3:
                print('Miércoles')
            case 4:
                print('Jueves')
            case 5:
                print('Viernes')
            case 6:
                print('Sábado')
            case 7:
                print('Domingo')
    except ValueError:
        print('El día de la semana no existe')
    except:
        print('error raro')
diaSemana()