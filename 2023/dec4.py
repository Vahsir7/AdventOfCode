input_file_path= r'D:\Coding\AdventOfCode\2023\Dec4input.txt'
with open(input_file_path, 'r', encoding='utf-8') as file:
    sum=0
    for s in file:
        s=s.strip()
        #print("test0")
        index=s.index(':')
        a=index-1

        #flex
        while(s[a].isdigit()):
            a-=1
        CardNumber=int(s[a+1:index])
        #print(CardNumber)
        
        winning = s[index+1:s.index("|")-1].split()
        myDraws = s[s.index("|")+1:].split()
        #print(winning)
        #print(myDraws)
        points=len(set(winning)&set(myDraws))
        #print(points)
        sum += int(2**(points-1))
print(sum)

