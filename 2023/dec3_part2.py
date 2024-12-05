def number(a,start):
    #print("a",a)
    i=start
    while(start>0):
        if(a[i].isdigit()):
            break
        i-=1
    start=i
    #print("check start",i)
    while(a[i].isdigit()):
        #print("finding end")
        i+=1
        if(i==len(a)):
            break
    end=i
    #print("end",end)
    i=start
    flag=False
    if(i-1>0 and a[i-1].isdigit()):
        i-=1
    while(a[i].isdigit()):
        flag=True
        i-=1
        #print("i",i)
        if(i==-1):
            break
    #print("i",i)
    if(flag):
        start=i+1
    #print("now start",start,"end",end)
    #print("hi :",a[start:end])
    return int(a[start:end])

def star_find(a, b, c):
    a = '.' + a + '.'
    b = '.' + b + '.'
    c = '.' + c + '.'
    sumres = 0
    i = 0
    print()
    while i < len(b):
        print(b[i],end="")
        #res=1
        y = 0
        hm=[]
        ta=tc=False
        if b[i] == "*":
            print()
            if a[i - 1].isdigit() :
                print("NW")
                print(number(a, i-1))
                #res *= number(a, i-1)
                hm.append(number(a, i-1))
                y += 1
                if(a[i].isdigit()):
                    ta=True
            if( a[i + 1].isdigit()) and not ta:
                print("NE")
                print(number(a, i+1))
                #res *= number(a, i+1)
                hm.append(number(a, i+1))
                y += 1
                if(a[i].isdigit()):
                    ta=True
            if a[i].isdigit() and y!=2 and not ta:
                print("N")
                print(number(a, i))
                #res *= number(a, i)
                hm.append(number(a, i))
                y += 1
                ta=True


            if c[i - 1].isdigit()  and y!=2:
                print("SW")
                print(number(c, i-1))
                #res *= number(c, i+1)
                hm.append(number(c, i-1))
                y += 1
                if(c[i].isdigit()):
                    tc=True 
            if  c[i + 1].isdigit() and y!=2 and not tc:
                print("SE")
                print(number(c, i+1))
                #res *= number(c, i+1)
                hm.append(number(c, i+1))
                y += 1
                if(c[i].isdigit()):
                    tc=True 
                tc=True
            if  c[i].isdigit() and y!=2 and not tc:
                print("S")
                print(number(c, i))
                #res *= number(c, i+1)
                hm.append(number(c, i))
                y += 1
                tc=True

            
            if b[i - 1].isdigit() and y != 2:
                print("W")
                print(number(b[:i], i-1))
                #res *= number(b[:i], i-1)
                hm.append(number(b[:i], i-1))
                y += 1
            if b[i + 1].isdigit() and y != 2:
                print("E")
                print(number(b[i + 1:], 1))
                #res *= number(b[i + 1:], 1)
                y+=1
                hm.append(number(b[i + 1:], 1))
        if y == 2:
            print("hm",hm[1],hm[0])
            sumres=sumres+(hm[1]*hm[0])
        i += 1
    return sumres

input_file_path=r'D:\Coding\AdventOfCode\2023\dec3input2.txt'
with open(input_file_path, 'r', encoding='utf-8') as file:
    SYMBOLS= "!@#$%^+&*[]-/<>?~`=,;:"
    arr=[]
    add=0
    num=len(file.readlines())
    file.seek(0)
    #print(num)
    arr.append(file.readline().strip())
    arr.append(file.readline().strip())
    arr.append(file.readline().strip())
    for i in range (1,num-1):
        #print("add",add, "at iteration ",i)
        #print(arr[1])
        add+=star_find(arr[0],arr[1],arr[2])
        arr[0]=arr[1]
        arr[1]=arr[2]
        arr[2]=file.readline().strip()
        #print("add",add)

print("ans",add)
