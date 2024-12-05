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
    #print("passed")
    #word=""
    if start!=0 : #if the number has a symbol before it 
        
        #print()
        #checks from top ajdacent postion of the sentence till end of the number
        for i in range(start-1,end): 
            #print(b[i],end="")
            #word+=b[i]
            if a[i] in SYMBOLS :
                #print(word)
                #print()
                return True
        
        #checks if before the number there is a symbol in the middle sentence
        
        if b[start-1] in SYMBOLS : 
            #print(b[start],end="")
            return True
        
        #word=""
        #checks from top ajdacent postion of the sentence till end of the number
        #print()
        #for i in range(start-1,end):
        #    print(b[i],end="")
        #print()
        for i in range(start-1,end): 
            #word=word+b[i]
            #print(b[i],end="")
            if c[i] in SYMBOLS :
                #print(word)
                return True
    else:

        #checks only from top and bottom of the middle sentence till end of the number
        for i in range(start-1,end):
            if a[i] in SYMBOLS or c[i] in SYMBOLS :
                return True     
    if end!=len(a) and (a[end] in SYMBOLS or c[end] in SYMBOLS or b[end] in SYMBOLS ):
        return True       
    return False

def find(a,z):
    """find(a,z) takes two arguments a and z
    a is a current 3 strings
    z is the type of checking done
        0 if we are checking the first sentence
        1 if we are checking in middle of the file
        2 if we are checking the last sentence
    """
    i=0
    res=0
    if(z==0): #current determines which sentence we are checking
        current=0 
    elif(z==1):
        current=1
    else:
        current=2

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

        #print(start,end)
        #order of passing is top sentence = a, middle sentence = b, bottom sentence = c
        if(start!=0 or end!=0) and z ==0 : 
            #passing a string of dots to nullify null effect at top
            if(check(start,end,'.'*len(arr[0]),a[0],a[1])): 
                res=res+int(a[current][start:end]) #if the number is valid then add it to the result

        elif(start!=0 or end!=0) and z ==1 :
            if check(start,end, a[0],a[1],a[2]):
                #print("ok:",a[current][start:end])
                res=res+int(a[current][start:end])

        elif (start!=0 or end!=0) and z ==2 :
            if check(start,end, a[1],a[2],"."*len(a[2])):
                res=res+int(a[current][start:end])
    return res


with open(r'D:\Coding\AdventOfCode\2023\dec3input.txt', 'r', encoding='utf-8') as file:
    
    SYMBOLS= r"!@#$%^&*()/\|{}[]<>?~`+=,;:'\""
    arr=[]
    add=0
    
    #print(arr)
    #print(len(arr[0]))
    
    num=len(file.readlines())
    file.seek(0)
    print(num)

    outer=0

    arr.append(file.readline().strip())
    arr.append(file.readline().strip())
    arr.append(file.readline().strip())

    add+=find(arr,0)

    while(outer<num-1):
        arr[0]=arr[1]
        arr[1]=arr[2]
        arr[2]=file.readline().strip()
        #print("ok: ",find(arr,1))
        add+=find(arr,1)
        outer+=1

    
    add+=find(arr,2)

    print(add)

        
            