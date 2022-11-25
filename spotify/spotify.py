#Diseñar una lista de spotify
mi_musica = {'un artista':{'una cancion':('rock',3,45),
                        'otra cancion':('salsa',3,27)},
            'otro artista':{}}


#Anexar canciones (genero, duracion) 1
def nueva_cancion(cancion,artista,genero,min,seg):
    if artista not in mi_musica:
        mi_musica[artista]={}
    if cancion in mi_musica[artista]:
        print ("---Esta cancion ya existe---")
    else:
        mi_musica[artista][cancion] = (genero,min,seg)
        print('---Cancion agregada correctamente---')
    input('---Enter para continuar---')

#Anexar artista 0
def nuevo_artista(artista):
    if artista in mi_musica:
        print ("---Este artista ya existe---")
    else:
        mi_musica[artista]={}
        print ('---Artista agregado correctamente---')
        tema = input('---Para agregar canciones digita "S"---')
        if tema == 'S' or 's':
            menu(1)

#Buscar artista 2
def buscar_artista(artista):
    if artista in mi_musica:
        for i,j in sorted(mi_musica[artista].items()):
            print(i,'// genero:',j[0],'// duracion:',j[1],':',j[2])
        input('---Enter para continuar---')
    else:
        input('---Artista no existe---')

#Buscar cancion 3
def buscar_cancion(cancion):
    for h,i in mi_musica.items():
        for j,k in i.items():
            if cancion not in j:
                input('---La cancion no existe---')
            elif j == cancion:
                print(h,j,k[0],sep='//',end='//')
                print(k[1],k[2],sep=':')
                input('---Enter para continuar---')
            else:
                input('---La cancion no existe---')

#eliminar artista 4
def eliminar_artista(artista):
    if artista in mi_musica:
        del mi_musica[artista]
        input('---Artista eliminado correctamente---')
    else:
        input('---Artista no existe---')

#Ordenar alfabeticamente 5
def ordenar():
    for h,i in mi_musica.items():
        for j,k in sorted(i.items()):
            print(j,h,k[0],sep='//',end='//')
            print(k[1],k[2],sep=':')
    input('---Enter para continuar---')
0
#Artista que tiene mas canciones 6
def mayor():
    max = 0
    for i,j in mi_musica.items():
        cant = len(j)
        if cant > max:
            max = cant
            fav = i
    print('tu artista favorita es:',fav)
            
#Artista que tiene la cancion mas larga 7
def larga():
    for i,j in mi_musica.items():
        largo = 0
        for l,k in j.items():
            tam = int(k[1]*60+k[2])
            fav = tam
            if tam > largo:
                largo = tam
                fav = l
        print(fav)

#Artista que tiene la cancion mas corta 8
def corta():
    for i,j in mi_musica.items():
        largo = 9999999
        for l,k in j.items():
            tam = k[1]*60+k[2]
            fav = tam
            if tam < largo:
                largo = tam
                fav = l
    print(fav)

#Menu
def menu(a):
    if a == 0:
        print ("Nombre del nuevo artista: ")
        artista = input()
        nuevo_artista(artista)
    if a == 1:
        print('Nombre del artista?')
        artista = input()
        print('Nombre de la nueva cancion: ')
        cancion = input()
        print('Genero?')
        genero = input()
        print('Cuantos minutos dura?')
        min = int(input())
        print('Cuantos segundos dura?')
        seg = input()
        nueva_cancion(cancion,artista,genero,min,seg)
    if a == 2:
        print ('Nombre del artista que buscas')
        artista = input()
        buscar_artista(artista)
    if a == 3:
        print('Nombre de la cancion que buscas')
        cancion = input()
        buscar_cancion(cancion)
    if a == 4:
        print('Nombre del artista que deseas eliminar')
        artista = input()
        eliminar_artista(artista)
    if a == 5:
        ordenar()
    if a == 6:
        mayor()
    if a == 7:
        larga()
    if a == 8:
        corta()

while True:
    print('-----------------------------------','     Bienvenido','   ¿Que deseas hacer hoy?',sep='\n')
    print('0 = Agregar nuevo artista','1 = Agregar nueva cancion','2 = Buscar artista','3 = Buscar cancion','4 = Eliminar un artista','5 = Ver tu lista de reproducción ordenada','6 = ¿Cual es mi artista favorito?','7 = ¿Cual es mi cancion mas larga?','8 = ¿Cual es mi cancion mas corta?','9 = SALIR',sep="\n")
    a = int(input())
    menu(a)
    if a == 9:
        break

print(mi_musica)