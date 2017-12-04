import random
def CreateTableWithRandomNumbers(n):
    table=[None]*n;

    for i in range(0,n):
        table[i]=random.randrange(0,100)
    return table
def CreateTable(n):
    table=[None]*n
    for i in range(0,n):
        table[i]=i+1
    random.shuffle(table)
    return table
def Swap(table,indexA,indexB):
    table[indexA], table[indexB] = table[indexB], table[indexA]

def BubbleSort(table):
    tableSize:int=len(table)
    for i in range(0,tableSize):
        for j in range(0,tableSize-i-1):
            if(table[j]>table[j+1]):
                Swap(table,j,j+1)


def InsertKey(table,begin,end,key):
    for i in range(end,begin-1,-1):
        if(key>=table[i]):
            table.insert(i+1,key)
            return
    table.insert(begin,key)

def InsertionSort(table):
    tableSize: int = len(table)
    for i in range(1,tableSize):
        element=table.pop(i)
        InsertKey(table,0,i-1,element)


table=CreateTable(100)
print(table,sep=" ")
InsertionSort(table)
print(table,sep=" ")