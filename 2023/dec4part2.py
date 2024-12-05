input_file_path= r'D:\Coding\AdventOfCode\2023\Dec4input.txt'
with open(input_file_path, 'r', encoding='utf-8') as file:
    SUM=0
    num=len(file.readlines())
    file.seek(0)
    numCards=[]
    Totpoints=[]
    
    for i in range(num):
        numCards.append(1)
    #print(numCards)
    for i in range(num):
        s=file.readline()
        s=s.strip()
        #print("test0")
        index=s.index(':')
        a=index-1
        while(s[a].isdigit()):
            a-=1
        CardNumber=int(s[a+1:index])
        #print(CardNumber)
        winning = s[index+1:s.index("|")-1].split()
        myDraws = s[s.index("|")+1:].split()
        #print(winning)
        #print(myDraws)
        points=len(set(winning)&set(myDraws))
        Totpoints.append(points)
        #print(points)
        SUM += int(2**(points-1))
        j=i+1
        while points>0:
            numCards[j]+=(1*numCards[i])
            points-=1
            j+=1

        #print(numCards)



#print(numCards)
#print(Totpoints)
print("part 1 :",SUM)
print("part 2:",sum(numCards))
