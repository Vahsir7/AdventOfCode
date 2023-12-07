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

    if start!=0 : #if the number has a symbol before it 
        for i in range(start-1,end): 
            if a[i] in SYMBOLS :
                #print(b[start:end])
                return True
        #checks if before the number there is a symbol in the middle sentence
        if b[start-1] in SYMBOLS : 
            #print(b[start:end])
            return True
        #checks from top ajdacent postion of the sentence till end of the number
        for i in range(start-1,end): 
            if c[i] in SYMBOLS :
                #print(b[start:end])
                return True
    else:
        #checks only from top and bottom of the middle sentence till end of the number
        for i in range(start-1,end):
            if a[i] in SYMBOLS or c[i] in SYMBOLS :
                #print(b[start:end])
                return True     
    if end!=len(a) and (a[end] in SYMBOLS or c[end] in SYMBOLS or b[end] in SYMBOLS ):
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
    current=1

    while i < len(a[current]):
        start = end = 0
        if a[current][i].isdigit():
            start = i
            while a[current][i].isdigit():
                i += 1
                if i == len(a[current]):
                    i -= 1
                    break
            end = i
        i += 1

        #order of passing is top sentence = a, middle sentence = b, bottom sentence = c

        if(start!=0 or end!=0):
            if check(start,end, a[0],a[1],a[2]):
                res=res+int(a[current][start:end])
    return res



with open('dec3_input.txt', 'r', encoding='utf-8') as file:
    SYMBOLS= r"!@#$%^&*()/\|{}[]<>?~`+=,;:'\""
    arr=[]
    add=0
    num=len(file.readlines())
    file.seek(1)
    arr.append(file.readline().strip())
    arr.append(file.readline().strip())
    arr.append(file.readline().strip())
    for i in range(1,num+2):
        add+=find(arr)
        arr[0]=arr[1]
        arr[1]=arr[2]
        arr[2]=file.readline().strip()

    print(add)