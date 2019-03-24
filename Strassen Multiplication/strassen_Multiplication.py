from tkinter import *
from tkinter import filedialog, scrolledtext
from functools import partial
import numpy as np
import easygui as eg

def fileReader():
    matA= filedialog.askopenfilename(filetypes =(("Text files",".txt"),("all files",".*")))
    matB= filedialog.askopenfilename(filetypes =(("Text files",".txt"),("all files",".*")))

    listaA = readFile(matA)
    listaB = readFile(matB)
    n = 0
    return listaA, listaB, n

def writeInText(a):
    if len(a)>16:
        file = open("matResult", 'w')
        for line in a:
            file.write(" ".join(str(elem) for elem in line) + "\n")
        file.close()
    else:
        pass

def button(window,label):
    intm1 ,intm2 ,n=fileReader()
    a = strassen(intm1,intm2)
    writeInText(a)
    label.config(text="")
    txt = scrolledtext.ScrolledText(window, width=600, height=400)
    txt.grid(column=0, row=1)
    mensaje = "Número de multiplicaciones: " + str(strassenMultiplications)
    eg.msgbox(msg=mensaje, title="Precaución", ok_button="Entendido")
    mensaje = "Matriz resultante: "
    eg.msgbox(msg=mensaje, title="Precaución", ok_button="Entendido")
    for i in a:
        txt.insert(INSERT, str(i) + "\n")

def button1(window, label):
    intm1,intm2,n=fileReader()
    a=multiplicateMatrix(intm1,intm2)
    writeInText(a)
    label.config(text="")
    txt = scrolledtext.ScrolledText(window, width=600, height=400)
    txt.grid(column=0, row=1)
    mensaje = "Número de multiplicaciones: " + str(multiplication)
    eg.msgbox(msg=mensaje, title="Precaución", ok_button="Entendido")
    mensaje = "Matriz resultante: "
    eg.msgbox(msg=mensaje, title="Precaución", ok_button="Entendido")
    for i in a:
        txt.insert(INSERT, str(i) + "\n")


def interface():
    window = Tk()
    window.title("PROYECTO")
    window.geometry('1080x900')
    label = Label(window, text="PROYECTO MATRICES: \n ", font=("Arial", 40), bg="blue")
    label.grid(column=0, row=0)
    btn = Button(window, text="Strassen-algorithm", command=lambda arg1=window, arg2=label: button(arg1, arg2),highlightbackground='#ffffff')
    print("")
    btn2 = Button(window, text="Por definición", command=lambda arg1=window, arg2=label: button1(arg1, arg2),
                  highlightbackground='#ffffff')
    label2 = Label(window, text="Rafael Moreno Cañas | A01378916 \n Marlon Brandon Velasco Pinello | A01379404",
                   font=("Arial", 10), bg="blue")

    label2.grid(column=0, row=20)
    btn.grid(column=0, row=12)
    btn2.grid(column=0, row=9)

    window.configure(background="blue")
    window.mainloop()


strassenMultiplications = 0

def readFile(filename):
    file = open(filename, 'r')
    row = [[int(num) for num in line.split(',')] for line in file]
    return (row)

def multiplicateMatrix(matA, matB):

    #Creamos la matriz Resultante
    matAxB = np.empty_like(matA)
    #Creamos un contador
    contador = 0
    tamañoA=len(matA)
    matBT = np.transpose(matB)
    #Comenzamos el ciclo para multiplicar AxB
    for index1 in range(tamañoA):
        for index2 in range(tamañoA):
            #creamos un acumulador
            acumulador = 0
            for index3 in range(tamañoA):
                contador+=1
                acumulador+= matA[index1][index3]*matBT[index2][index3]
            matAxB[index1][index2]=acumulador
    #mensaje = "Número de calculos: " + str(contador)
    #eg.msgbox(msg=mensaje, title="Precaución", ok_button="Entendido")
    #multiplication = contador
    global multiplication
    multiplication=contador
    return (matAxB)


def matrix_addition(matrix_a, matrix_b):
    # print(matrix_a)
    return [[matrix_a[row][col] + matrix_b[row][col]
             for col in range(len(matrix_a[row]))] for row in range(len(matrix_a))]


def matrix_subtraction(matrix_a, matrix_b):
    return [[matrix_a[row][col] - matrix_b[row][col]
             for col in range(len(matrix_a[row]))] for row in range(len(matrix_a))]


def split_matrix(a):
    """
    Given a matrix, return the TOP_LEFT, TOP_RIGHT, BOT_LEFT and BOT_RIGHT quadrant
    """
    if len(a) % 2 != 0 or len(a[0]) % 2 != 0:
        raise Exception('Odd matrices are not supported!')

    matrix_length = len(a)
    mid = matrix_length // 2
    top_left = [[a[i][j] for j in range(mid)] for i in range(mid)]
    bot_left = [[a[i][j] for j in range(mid)] for i in range(mid, matrix_length)]

    top_right = [[a[i][j] for j in range(mid, matrix_length)] for i in range(mid)]
    bot_right = [[a[i][j] for j in range(mid, matrix_length)] for i in range(mid, matrix_length)]

    return top_left, top_right, bot_left, bot_right


def get_matrix_dimensions(matrix):
    return len(matrix), len(matrix[0])


def strassen(matrix_a, matrix_b):
    """
    Recursive function to calculate the product of two matrices, using the Strassen Algorithm.
    Currently only works for matrices of even length (2x2, 4x4, 6x6...etc)
    """
    if get_matrix_dimensions(matrix_a) != get_matrix_dimensions(matrix_b):
        raise Exception(f'Both matrices are not the same dimension! \nMatrix A:{matrix_a} \nMatrix B:{matrix_b}')
    global strassenMultiplications
    strassenMultiplications += 7
    if len(matrix_a) == 2:
        return multiplicateMatrix(matrix_a, matrix_b)

    A, B, C, D = split_matrix(matrix_a)
    E, F, G, H = split_matrix(matrix_b)

    p1 = strassen(A, matrix_subtraction(F, H))
    p2 = strassen(matrix_addition(A, B), H)
    p3 = strassen(matrix_addition(C, D), E)
    p4 = strassen(D, matrix_subtraction(G, E))
    p5 = strassen(matrix_addition(A, D), matrix_addition(E, H))
    p6 = strassen(matrix_subtraction(B, D), matrix_addition(G, H))
    p7 = strassen(matrix_subtraction(A, C), matrix_addition(E, F))

    top_left = matrix_addition(matrix_subtraction(matrix_addition(p5, p4), p2), p6)
    top_right = matrix_addition(p1, p2)
    bot_left = matrix_addition(p3, p4)
    bot_right = matrix_subtraction(matrix_subtraction(matrix_addition(p1, p5), p3), p7)

    # construct the new matrix from our 4 quadrants
    new_matrix = []
    for i in range(len(top_right)):
        new_matrix.append(top_left[i] + top_right[i])
    for i in range(len(bot_right)):
        new_matrix.append(bot_left[i] + bot_right[i])
    return new_matrix

def main():
    global strassenMultiplications
    matA = readFile('03. Matrix_A_128_2_7.txt')
    matB = readFile('04. Matrix_B_128_2_7.txt')
    multiplications, matResult = default_matrix_multiplication(matA, matB)

    print(matResult)
    print(multiplications)
    print(strassenMultiplications)
    print(matA)
    print(matB)

interface()

