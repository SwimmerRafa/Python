# Autores: 
#          Omar Cruz Flores A01379963
#          Rafael Moreno Cañas A01378916 
#
# Desliza números.
#
# 5 de mayo, 2017.
from os.path import exists
from time import strftime
import random

def juego(m):
    imprime_cuadricula(m)
    s=input("Selecciona una opción ([A]rriba, a[B]ajo, [I]zquierda, [D]erecha, [S]alir): ")
    print()
    while s not in "DdIiBbAaSs" or s=="":
        print("\n" + "Haz colocado un carácter invalido"+"\n")
        s=input("Selecciona una opción ([A]rriba, a[B]ajo, [I]zquierda, [D]erecha, [S]alir): ")
        print()
    while s not in("Ss"):
        if s in "Dd":
            m, z=uno_azar(matriz_vieja(m), right_mov(m))
        if s in "Ii":
            m,z=uno_azar(matriz_vieja(m), left_mov(m))
        if s in "Bb":
            m,z=uno_azar(matriz_vieja(m), down_mov(m))
        if s in "Aa":
            m,z=uno_azar(matriz_vieja(m), up_mov(m))
        if z==True:
            imprime_cuadricula(m)
            puntaje(m)
        imprime_cuadricula(m)
        s=input("Selecciona una opción ([A]rriba, a[B]ajo, [I]zquierda, [D]erecha, [S]alir): ")
        print()
        while s not in "DdIiBbAaSs" or s=="":
            print("Haz colocado un carácter invalido"+"\n")
            s=input("Selecciona una opción ([A]rriba, a[B]ajo, [I]zquierda, [D]erecha, [S]alir): ")
            print()
    puntaje(m)
                    
def imprime_cuadricula(m):
    raya = '+' + ('-' * 6 + '+') * 4
    print(raya)
    for i in range(4):
        print('|', end='')
        for j in range(4):
            if m[i][j]==0:
                m[i][j]=""
            print('{0:5}'.format(m[i][j]), end=' |')
            if m[i][j]=="":
                m[i][j]=0
        print()
        print(raya)   
        
def matriz_vieja(m):
    r = []
    for ren in m:
        r.append(ren[:])
    return r
    
def uno_azar(m, z):#checa si el movimiento es valido y agrega uno si no es un tiro invalido.
    if m!=z:
        n=0
        for l in z:
            if 0 in l:
                n+=1
        if n>0:
            mat=[0,1,2,3]
            s=random.choice(mat)
            k=random.choice(mat)       
            while z[s][k]!=0:
                s=random.choice(mat)
                k=random.choice(mat)
                z[s][k]
            z[s][k]=1
            return z, False
        return fin(z)
        
    for i in range(4):
        for j in range(4):
            if z[i][j] == 0:
                print("TIRO NULO INTENTALO DENUEVO." + "\n")
                return z, False 
            
    else:
        return fin(z)

def fin(m):
    for i in range(4):
        for j in range(4):
            # ¿Mi vecino de la derecha es igual a mí?
            if j < 3 and m[i][j] == m[i][j + 1]:
                print("TIRO NULO INTENTALO DENUEVO." + "\n")
                return m, False
            # ¿Mi vecino de abajo es igual a mí?
            if i < 3 and m[i][j] == m[i + 1][j]:
                print("TIRO NULO INTENTALO DENUEVO." + "\n")
                return m, False
    print("FIN DEL JUEGO." + "\n")
    return m, True
          
def right_mov(m):
    l=[3,2,1]
    li=[3,2,1,0]
    for k in l:
        for z in li:
            if m[z][k]==m[z][k-1] or m[z][k]==0:
                m[z][k]+=m[z][k-1]
                m[z][k-1]=0    
    return m  

def left_mov(m):
    l=[0,1,2]
    li=[0,1,2,3]
    for k in l:
        for z in li:
            if m[z][k]==m[z][k+1] or m[z][k]==0:
                m[z][k]+=m[z][k+1]
                m[z][k+1]=0
    return m
    
def down_mov(m):
    l=[2,1,0]
    li=[0,1,2,3]
    for k in l:
        for z in li:
            if m[k][z]==m[k+1][z] or m[k+1][z]==0:
                m[k+1][z]+=m[k][z]
                m[k][z]=0 
    return m
    
def up_mov(m):
    l=[0,1,2]
    li=[0,1,2,3]
    for k in l:
        for z in li:
            if m[k][z]==m[k+1][z] or m[k][z]==0:
                m[k][z]+=m[k+1][z]
                m[k+1][z]=0
    return m

def jugar():
    m=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    mat=[0,1,2,3]
    s=random.choice(mat)
    k=random.choice(mat)
    m[s][k]=1
    juego(m)                 

def menu_principal():
    print("**  DESLIZA NÚMEROS  **")
    print()
    print("       Menú        ")
    print("===================")
    print("1. Jugar")
    print("2. Puntajes")
    print("3. Salir")
    print("===================")
    print()

#-----------------------puntaje funciones------------------------------------
def puntaje(m):
    l1=sum(m[0])
    l2=sum(m[1])
    l3=sum(m[2])
    l4=sum(m[3])
    punt=l1+l2+l3+l4
    print("Fin de juego" +"\n")
    print("Puntaje obtenido: ", punt)
    print()
    guardar=input("¿Deseas guardar este puntaje? ([S]i, [N]o): ")
    print()
    if guardar in "Ss":
        name= str(input("Ingresa tu nombre: "))
        name = name[0:9]
        print()
        print("Tu puntaje quedo registrado." +"\n")
        puntajejug(punt, name)
        print()
    elif guardar in"Nn":
        print()
    else: 
        print("No te entiendo, vamos al menú" + "\n")

def puntajejug(punt, name):
    n=0
    fecha_y_hora = strftime('%Y-%m-%d %H:%M:%S')
    l=[]
    l.append(punt)
    l.append(name)
    l.append(fecha_y_hora)
    x=guard(l)
    for j in range(len(x)):
        n+=1
        x[j].insert(0,n)

    with open("puntajes.txt", "w") as f:
        for k in range(len(x)):
            for i in range(len(x[0])):
                s=str(x[k][i])
                if i==0:
                    
                    f.write("{0: >5}".format(s))
                if i==1:
                    
                    f.write(" {0: >6}".format(s))
                if i==2:
                    
                    f.write("   {0:9}  ".format(s))
                if i==3:
                    f.write(s)
            f.write("\n")
    
def menu_puntaje():
    if not exists('puntajes.txt'):
        print('Puntajes no encontrados!')
        print("\n")
    else:
        print("== Tabla de puntajes ==")
        print()
        print("Lugar Puntaje  Usuario    Fecha y hora")
        print("----- -------  ---------- -------------------")
        with open("puntajes.txt", "r") as z:
            print(z.read())
        print("----- -------  ---------- -------------------")
        print()
    
    
def guard(l):
    if not exists('puntajes.txt'):
        lista=[]
        lista.append(l)
        
    else:
        lista=[]
        with open("puntajes.txt", "r") as f:
            s=f.readlines()
            
        for k in range(len(s)):
            m=s[k].split()
            if len(m)==6:
                m[2]+=" "+m[3]
                m[3]=m[4]
                del m[4]
            for j in range(len(m)):
                if j==0:
                    del m[j]
                if j==0:
                    m[j]=int(m[j])
            
            m[2]+=(" "+ m[3])
            del m[3]
            
            lista.append(m)
        lista.append(l)
        
    return sorted(lista, reverse=True)
    
    
def main():
    while True:
        menu_principal()
        op = input('Selecciona una opción(1-3): ')
        print()
        if op == "1":
            jugar()
        elif op == "2" :
            menu_puntaje()       
        elif op == "3": 
            break
        else:
            print("No es un carácter válido." + "\n")
    print("Hasta la vista, baby.")

main()