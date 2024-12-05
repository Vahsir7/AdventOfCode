def check(a,b,c,start,end):
    '''
        check(a,b,c,start,end) takes 5 arguments
        a,b,c are strings
        start and end are integers
        
        this functions checks if any symbols are surrounding the number 
        considering a b c to be an matrix of characters
    '''
    #print("\n\n")
    #if(len(a)==len(b)==len(c)):
    #    print("true")
    #    print(b[start:end])
    #    print(start,end,len(a))
    if(start-1>0):
    #    print("beginning")
        if b[start-1] in SYMBOLS or a[start-1] in SYMBOLS or c[start-1] in SYMBOLS:
            return True
            
    if(end!=len(a)):
    #    print("end")
        if b[end] in SYMBOLS or a[end] in SYMBOLS or c[end] in SYMBOLS:
            return True
    for i in range(start,end):
        if a[i] in SYMBOLS or c[i] in SYMBOLS:
             return True
    #print("nein")
    return False

def find(a):
    i=0
    res=0
    while(i<len(a[1])):
        if(a[1][i].isdigit()):
            start=i
            while(a[1][i].isdigit()):
                i+=1
                if(i==len(a[1])):
                    break
            end=i
            if(check(a[0],a[1],a[2],start,end)):
                print(a[1][start:end])
                res+=int(a[1][start:end])
        i+=1
    return res

input_file_path=r'D:\Coding\AdventOfCode\2023\dec3input.txt'
'''
with open(input_file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()
line_length = len(lines[0].strip())
lines.insert(0, '.' * line_length + '\n')
lines.append('.' * line_length + '\n')
with open(input_file_path, 'w', encoding='utf-8') as file:
    file.writelines(lines)

'''
with open(input_file_path, 'r', encoding='utf-8') as file:
    SYMBOLS= "!@#$%^+&*[]-/<>?~`=,;:"
    arr=[]
    add=0
    num=len(file.readlines())
    file.seek(0)
    arr.append(file.readline().strip())
    arr.append(file.readline().strip())
    arr.append(file.readline().strip())
    for i in range (1,num):
        add+=find(arr)
        arr[0]=arr[1]
        arr[1]=arr[2]
        arr[2]=file.readline().strip()

print(add)

        
        