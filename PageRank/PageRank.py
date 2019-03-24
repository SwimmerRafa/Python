def main():
    while True:
        menu_principal()
        op = input('Select one choice(1/2): ')
        print()
        if op == '1':
            pageRank()

        elif op == '2':
            print('Bye !')
            return
        else:
            print('Ivalid input.')
            print()

def menu_principal():
    print('''     
    ____                      ____              __  
   / __ \____ _____ ____     / __ \____ _____  / /__
  / /_/ / __ `/ __ `/ _ \   / /_/ / __ `/ __ \/ //_/
 / ____/ /_/ / /_/ /  __/  / _, _/ /_/ / / / / ,<   
/_/    \__,_/\__, /\___/  /_/ |_|\__,_/_/ /_/_/|_|  
            /____/                                

    by: Rafael Moreno

    ------------------------------------------------------
    (1) Page Rank
    (2) Exit
    ------------------------------------------------------
        ''')

def nodo():
    try:
        name = input('Give me the name of the node : ')
        inlinks = int(input('Give me the number of the INLINKS of the node '+str(name)+': '))
        outlinks = int(input('Give me the number of the OUTLINKS of the node '+str(name)+': '))
        print()
    except Exception as e:
        print(e)
        return nodo()
    inList = []
    for i in range(1, inlinks+1):
        temp = input('Give me the  '+str(i)+'° node that enters '+str(name)+': ')
        inList.append(str(temp))
    retList = [name, inlinks, outlinks, inList]
    return retList


def pageRank():
    global numNodes
    try:
        print(("=") * 23 + " SYSTEM VALUES " + ("=") * 23)
        print()
        numNodes = int(input('Give me the number of nodes of the system: '))
        itera=int(input('Give me the number of rounds/iterations: '))
    except Exception as e:
        print(e)
        return pageRank()
    r0=round((1/numNodes),2)
    listNodes=[]
    nameNodeList=[]
    rowIterList=[]
    for i in range(numNodes):
        print()
        print(("=") * 23 + " NODE " + str(i+1) + " " + ("=") * 23)
        newNode=nodo()
        name=newNode[0]
        listNodes.append(newNode)
        nameNodeList.append(name)
        rowIterList.append([r0])
    for i in range(1,itera):
        for node in listNodes:
            indexNode=nameNodeList.index(node[0])
            r=0
            for entradas in node[3]:
                index=nameNodeList.index(entradas)
                r+=round(((rowIterList[index][-1])/(listNodes[index][2])),2)
            rowIterList[indexNode].append(round(r,2))
    lastIter=[]
    rankList=[]
    for i in rowIterList:
        lastIter.append(i[-1])
        rankList.append(0)
    lastIterOrder=sorted(lastIter,reverse=True)
    rank=0
    readed=[]
    for i in range(len(lastIterOrder)):
        maximo=lastIterOrder[i]
        indexMax=lastIter.index(maximo)
        if not lastIter[indexMax] in readed:
            rank+=1
            readed.append(lastIter[indexMax])
            lastIter[indexMax]='@'
            rankList[indexMax]=rank
        else:
            readed.append(lastIter[indexMax])
            lastIter[indexMax]='@'
            rankList[indexMax]=rank
    print()
    print(("=") * 46)

    print('''    
          _____             _    
         |  __ \           | |   
         | |__) |__ _ _ __ | | __
         |  _  // _` | '_ \| |/ /
         | | \ \ (_| | | | |   < 
         |_|  \_\__,_|_| |_|_|\_\
         
    n = nodes
    in = inlinks
    out = outlinks
                         
            ''')
    print()
    print("[n, in, out] [--ITERACIONES--] [rank]")
    for i in range(len(listNodes)):
        print(listNodes[i][:3], rowIterList[i], rankList[i])
    print(("=") * 46)
main()