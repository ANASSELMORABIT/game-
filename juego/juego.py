juego=[
        [" -"," -"," -"],
        [" -"," -"," -"],
        [" -"," -"," -"]
    ]
def tabla(juego):
    print("0|  1  2  3")
    print("\n")
    for i,value in enumerate(juego):
        print(f"{i+1}|",end=" ")
        for j in range(len(juego)):
            print(f"{value[j]}",end=" ")
        print("\n")
    return
def jugadores():
    jugadorX=input("The first player (X):")
    jugadorO=input("The second player (O):")
    return jugadorX,jugadorO
posicionX=0
posicionO=0
def posicion_PlayerX(posicionX,posicionO):
    print("The first Player(X):")
    posicionX=int(input("give me the posicion:"))
    posicion1X=posicionX // 10
    posicion2X=posicionX % 10
    while (posicion1X>3 and posicion1X<1 and posicion2X >3 and posicion2X<1 and posicionX==posicionO ):
        print("invalid posicion")
        posicionX=int(input("give me a valid  posicion:"))
        posicion1X=posicionX // 10
        posicion2X=posicionX % 10
    return posicion1X,posicion2X
def posicion_PlayerO(posicionX,posicionO):
    print("The second Player(X):")
    posicionO=int(input("give me the posicion:"))
    posicion1O=posicionO // 10
    posicion2O=posicionO % 10
    while (posicion1O>3 and posicion1O<1 and posicion2O >3 and posicion2O<1 and posicionX==posicionO ):
        print("invalid posicion")
        posicionO=int(input("give me a valid  posicion:"))
        posicion1O=posicionO // 10
        posicion2O=posicionO % 10
    return posicion1O,posicion2O
player1,player2=jugadores()
X1,X2=posicion_PlayerX(posicionX,posicionO)
juego[X1-1][X2-1]=" X"
tabla(juego)
O1,O2=posicion_PlayerO(posicionX,posicionO)
juego[O1-1][O2-1]=" O"
tabla(juego)
tabla(juego)