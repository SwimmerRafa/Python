# Autores: 
#          Rafael Moreno Cañas A01378916
#
# El juego consiste en que el jugador descifre un código secreto conformado de T caracteres
# tomados de L letras distintas y teniendo como límite un máximo número de intentos M 
# (en donde 2 ≤ T ≤ L ≤ 26, y 1 ≤ M ≤ 99).
#
# En cada juego, el programa selecciona al azar el código secreto y le solicita al jugador que 
# escriba su primer intento. El jugador teclea una cadena de T caracteres. El programa 
# reporta cuántas letras fueron acertadas, tanto en posiciones incorrectas como correctas. 
# El juego continúa así hasta que el jugador acerte todas las letras y posiciones, o haya 
# utilizado sus M intentos. En caso de que el jugador pierda, el programa le muestra cuál era 
# el código secreto.
#
# Noviembre 30, 2016.

from random import shuffle
from os.path import exists

letras = ['a', 'b', 'c','d', 'e', 'f', "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r"
            , "s", "t", "u", "v", "w", "x", "y", "z"]

def configuracion():
     if exists("configuracion.txt"):
         with open ("configuracion.txt") as predeter :
             T= int(predeter.readline())
             L= int(predeter.readline())
             M= int(predeter.readline())
    
     else:
         T = 4
         L = 6
         M = 10
         with open ("configuracion.txt", "w") as predeter :
                predeter.write(str(T) + '\n')
                predeter.write(str(L) + '\n')
                predeter.write(str(M) + '\n')
     return T, L, M

def config_nueva():
    T = input("longitud del código a romper: ")
    while not T.isdigit() or int(T) <2 or int(T) >26:
        print(T, "no es un número entero positivo válido.")
        T= input("Longitud del código a romper: ")
    L = input('Letras distintas posibles: ')
    while not L.isdigit() or int(L) < int(T) or int(L) > 26:
        print('El número debe de estar entre', T, 'y 26.')
        L = input("Letras distintas posibles: ")
    M = input("Máximo número de intentos: ")
    while not M.isdigit() :
        print(M, 'no es un número entero positivo válido.')
        M = input("Máximo número de intentos: ")
    while  int(M) < 1 or int(M) > 99 :
        print('El número debe estar entre 1 y 99.')
        M = input("Máximo numero de intentos: ")    
    with open ("configuracion.txt", "w") as config_nueva :
        config_nueva.write(str(T) + '\n')
        config_nueva.write(str(L) + '\n')
        config_nueva.write(str(M)+ '\n')
    print()
    print('Los cambios han sido guardados exitosamente')
    main()
    
def escoge_letras():
    T, L, M = configuracion()
    aleatorio = ''
    let = letras [:L]
    shuffle(let)
    for i in let [0: T]:
        aleatorio += i
    return aleatorio

def letras_validas(a, validas):
    for letras in a:
        if letras not in validas:
            return False
    return True
    
def jugar():
    T, L, M = configuracion()
    intentos = M
    codigo = escoge_letras()
    intentos_totales = 0
    validas = letras [:L]
    
    print()
    print("El número restante para romper él código es: ", intentos)
    print()
    while True:       
        while True:
            print("Teclea una cadena de", T, "caracteres de la", letras[0].upper(), "a", letras [L -1].upper(), end = "")
            x = input(': ').lower()
            a = list(x)
            b = list(set(a))
            if len (a) == len(b):
                if len(x) == T :  
                    if letras_validas(x, validas):
                        break
                    else:
                        print("Carácter inválido")
                else:
                    print('La cadena debe contener exactamente', T, 'caracteres.')
            else:
                print("La cadena no debe tener caracteres repetidos")
        intentos -= 1
        intentos_totales += 1
        correctas = 0
        coinsidencias = 0
        for p in range (T):
           if x[p] == codigo[p]:
               correctas += 1
           elif x[p] in codigo :
            coinsidencias += 1
        print()
        print("Letras en la posición correcta: ", correctas)
        print("Coinsidencias en el código: ", coinsidencias)
        print()
        print("Intentos restantes: ", intentos)
        print()
        if x == codigo or intentos == 0:
            break
         
    if x == codigo :
        print("Felicidades rompiste el código en", intentos_totales, "intentos.")
    elif intentos == 0:
        print("Pérdiste, el código a romper era", codigo.upper())

def menu_principal():
    print("**  ROMPE CÓDIGOS  **")
    print()
    print("       Menú        ")
    print("===================")
    print("1. Jugar")
    print("2. Configuración")
    print("3. Salir")
    print("===================")
    print()
       
def main():
    while True:
        menu_principal()
        op = input('Selecciona una opción: ')
        print()
        if op == '1':
            jugar()
        
        elif op == '2':
            print()
            print ('------Configuración------')
            print()
            T, L, M = configuracion()
            print('Longuitud del código a romper:', T)
            print('Letras distintas posibles: ', L)
            print('Máximos de intentos posibles: ', M)
            print()
            x = input('¿Desea modificar estos valores? (s/n) : ')
            print()
            while True:
                if x.lower() == "s" :
                    config_nueva()
                    print()
                elif x.lower() == "n" :
                    return main()
                else :
                    print('No es una opción válida.')
                    x = input('¿Desea modificar estos valores? (s/n): ')
                print()
       
        elif op == '3': 
            print('Bye !')
            return
        else:
            print('No es una opción válida.')

main()