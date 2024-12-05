import math
input_file_path = r"D:\Coding\AdventOfCode\2023\dec8input.txt"
with open(input_file_path, "r", encoding="utf-8") as f:
    directions = f.readline().strip()
    directions=directions.replace("R", "1")
    directions=directions.replace("L", "0")
    #print(directions)
    f.readline()
    network = {}
    currentNode=[]
    for line in f:
        line = line.strip()
        a,b,c=line[:3],line[7:10],line[12:15]
        if(a[-1]=="A"):
            currentNode.append(a)
        network[a] = (b,c)
    
    print(currentNode)
    #print(network)
    #print(len(directions))
    

    
    
    totalSteps=[]
    for j in currentNode:
        CN=j
        i=0
        steps=0

        while(CN[-1]!="Z"):
            
            #print("i",i)
            #print("currentNode",currentNode)
            #print("moving",directions[i])
            steps+=1
            CN = network[CN][int(directions[i])]
            i=(i+1)%(len(directions))
        totalSteps.append(steps)
    
a=totalSteps[0]
for i in totalSteps:
    a=math.lcm(a,i)
print("steps:",a)
        