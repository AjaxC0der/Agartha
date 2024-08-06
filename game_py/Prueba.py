import diccionarios as DC

JUEGO = True
PARTIDA = False
MENU = True
ENTRADA = None
INFORMACION_JUEGO = False


while JUEGO:
    while MENU:
        ENTRADA = input("""
1- Partida Nueva\n
2- Continuar Partida\n
3- Acerca de...\n
4- Salir
""")
        if ENTRADA == 1:
            MENU = False
            PARTIDA = True
        elif ENTRADA == 2:
            print("Por ahora no esta implementado")
        elif ENTRADA == 3:
            MENU = False
            INFORMACION_JUEGO = True
        elif ENTRADA == 4:
            quit()
        else:
            print("Vuelva a introducir una entrada valida")

    while INFORMACION_JUEGO:
        entrada = input("""
1- Como Jugar
2- Informacion del juego
3- Quien lo creo
4- Menu Principal
""")
        if entrada == 1:
            print("Para jugar lo mejor que puede hacer es no tener miedo")
        elif entrada == 2:
            print("Este juego es una copia de zork lo que llevada al extremo")
        elif entrada == 3:
            print("El creador es Ajax")
        elif entrada == 4:
            print("Volviendo al menu...")
            INFORMACION_JUEGO = False
            MENU = True
        else:
            print("Vuelva a introducir una entrada valida")
    while PARTIDA:
        print("Estas en el juego")
