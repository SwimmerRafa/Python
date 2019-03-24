#In order to run this program you must install pandas and tabulate with the following commands :
#pandas: "pip install pandas"
#tabulate: "pip install tabulate"

import pandas as pd
from itertools import combinations
from tabulate import tabulate

def main():
    while True:
        menu_principal()
        op = input('Select one option(1/2): ')
        print()
        if op == '1':
            nfa_dfa()
        elif op == '2':
            print('Bye !')
            return
        else:
            print('Invalid input.')
            print()


def menu_principal():
    print("**                     NFA ---> DFA                 **")
    print()
    print("**              Rafael Moreno | A01379816           **")
    print()
    print("MENU")
    print("======================================================")
    print("SELECT ONE CHOICE")
    print()
    print("1. Covert NFA to DFA")
    print("2. Exit")
    print()
    print("======================================================")
    print()





def nfa_dfa():
    try:
        usr_states = int(input("Give me the number of states: "))
        usr_alphabet= int(input("Give me the number of elements of the alphabet: "))
    except Exception as e:
        print("Something goes wrong" + "\n Error: " + str(e))
        return nfa_dfa()

    states = []
    alphabet = []

    #The user is asked to inpput the states
    print()
    print(("=") * 23 + " STATES " + ("=") * 23)
    print(" NOTE: THE ALPHABET MUST CONTAIN ONLY ONE CHARACTER")
    print()
    for i in range(1, usr_states + 1):
        x = input(str(i) + "° state: ")
        while len(x) != 1:
            print("Please input only one character")
            x = input(str(i) + "° state: ")
        states.append(x)

    #The user is asked to input the alphabet
    print()
    print(("=") * 23 + " ALPHABET " + ("=") * 23)
    print()
    for i in range(1, usr_alphabet+ 1):
        x = input(str(i) + "° element of the  alphabet: ")
        while len(x) != 1:
            print("Please input only one character")
            x = input(str(i) + "° element of the  alphabet: ")
        alphabet.append(x)

    #The user assigns the transition table
    print()
    print(("=") * 10 + " TRANSITION TABLE OF THE NFA" + ("=") * 10)
    print("The empty set is asigned with the character ´&´ ")
    print()
    usr_matrix = []
    for i in range(usr_states):
        x = []
        for j in range(usr_alphabet):
            y = input("%s recives %s: " %(states[i], alphabet[j]))
            while len(y) < 1:
                print("Please input something")
                print()
                y = input("%s recives %s: " %(states[i], alphabet[j]))
            x.append(y)
        usr_matrix.append(x)

    #The tabulates generate the NFA transition table
    print()
    print(("=") * 22 + " NFA TABLE" + ("=") * 22)
    print()
    print(tableCreator(states,alphabet,usr_matrix))
    print()
    print()


    #Start changing nfa to dfa

    dfa_states = []

    #Obtain all combinatios with function combinatios
    for i in range(1, len(states) + 1):
        combination_list = list(combinations(toString(states), i))
        for j in combination_list:
            dfa_states.append(list(j))

    #Start changing nfa to dfa
    dfa_states = []

    #Obtain all combiantions posible with the function combination
    for i in range(1, len(states) + 1):
        combList = list(combinations(toString(states), i))
        for j in combList:
            dfa_states.append(list(j))

    dfa_matrix = []

    #Get values of the urs_matrix
    for state in dfa_states:
        dataList = []
        for single in state:
            data = getData(single, states, usr_matrix)
            dataList.append(data)

        completeData = []

        # Join the values of each combination
        for i in range(usr_alphabet):
            completeData.append('')
            for data in dataList:
                if completeData[i] == '' and data[i] != '&':
                    completeData[i] += data[i]
                elif data[i] != '&' and completeData[i].find(data[i]) == -1:
                    completeData[i] += ',' + data[i]
                else:
                    pass

        dfa_matrix.append(completeData)

    for i in dfa_matrix:
        for j in range(len(i)):
            if i[j] == '':
                i[j] = '&'

    print('\n' + ('=' * 15 + 'DFA TABLE' + ('=') * 15) + '\n')
    print(tableCreator(dfa_states,alphabet,dfa_matrix))


def toString(list):
    list_string = ''
    for i in list:
        list_string += str(i)
    return list_string

def tableCreator(states, alphabet, matrix):
    try:
        data = {'S/A': states}
        for i in range(len(alphabet)):
            x = []
            for j in matrix:
                x.append(j[i])
            data.update({str(alphabet[i]): x})
        table = pd.DataFrame(data)
        return str(tabulate(table, headers='keys', tablefmt='grid', showindex=False))
    except Exception as e:
        return e

def getData(s_state, states, matrix):
    ind = states.index(str(s_state))
    data = matrix[ind]
    return list(data)

main()