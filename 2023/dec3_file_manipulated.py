"""
https://adventofcode.com/2023/day/3
gear ratio problem
"""

def check(start,end,a,b,c):

    '''
    function check(start,end,a,b,c) takes 5 arguments
    start is the starting index of the number
    end is the ending index of the number
    a,b,c are the 3 strings
    returns True if the number is valid else returns False
    '''
    #print("num: ", a[start:end])
    #print("num: ", b[start:end])
    #print("num: ", c[start:end])
    if b[start:end][-1] in SYMBOLS:
        return True
    if(start!=0):
        if b[start-1] in SYMBOLS :
            return True
    if start!=0 and end!=len(a): #if the number has a symbol before it
        for i in range(start-1,end):
            #print(a[i])
            if a[i] in SYMBOLS :
                #print(b[start:end])
                return True
        #checks if before the number there is a symbol in the middle sentence
        #checks from top ajdacent postion of the sentence till end of the number
        for j in range(start-1,end):
            #print(c[j])
            if c[j] in SYMBOLS :
                #print(b[start:end])
                return True
    else:
        #checks only from top and bottom of the middle sentence till end of the number
        print(b[start:end])
        for i in range(start-1,end):
            #print(a[i])
            if a[i] in SYMBOLS or c[i] in SYMBOLS :
                
                return True 
    #print("len a",len(a),"end"  ,end)    
    if (end)==len(a) and (a[end-1] in SYMBOLS or c[end-1] in SYMBOLS):
        #print(b[start:end])
        return True       
    return False

def find(a):
    """
        find(a) takes one argument a
        a is an array of 3 strings
        returns the sum of all the valid numbers in the middle string
        start if the starting index of the number 
        end is the ending index of the number
    """
    i=0
    res=0
    while i < len(a[1]):
        start = end = 0
        if a[1][i].isdigit():
            #print("true")
            start = i
            while a[1][i].isdigit():
                #print(a[1][i])
                i += 1
                if i == len(a[1]):
                    #print("huh")
                    i -= 1
                    break
            
            end = i+1
            #print(start,end)
        if(start!=0 or end!=0):
            #print(a[1][start:end])
            if check(start,end, a[0],a[1],a[2]):
                if(a[1][end-1]=='.' or a[1][end-1] in SYMBOLS):
                    end-=1
                print(a[1][start:end])
                res+=int(a[1][start:end])
        i += 1

        #order of passing is top sentence = a, middle sentence = b, bottom sentence = c
    return res



with open(r'D:\Coding\AdventOfCode\2023\dec3input.txt', 'r', encoding='utf-8') as file:
    SYMBOLS= "!@#$%^+&*[]/<>?~`=,;:"
    arr=[]
    add=0
    num=len(file.readlines())
    file.seek(0)
    arr.append(file.readline().strip())
    arr.append(file.readline().strip())
    arr.append(file.readline().strip())
    for i in range(1,num+2):
        add+=find(arr)
        arr[0]=arr[1]
        arr[1]=arr[2]
        arr[2]=file.readline().strip()

    print(add)