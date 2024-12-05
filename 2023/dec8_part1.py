input_file_path = r"D:\Coding\AdventOfCode\2023\dec8input.txt"
with open(input_file_path, "r", encoding="utf-8") as f:
    directions = f.readline().strip()
    directions=directions.replace("R", "1")
    directions=directions.replace("L", "0")
    #print(directions)
    f.readline()
    network = {}
    for line in f:
        line = line.strip()
        a,b,c=line[:3],line[7:10],line[12:15]
        network[a] = (b,c)
    
    print(network)
    #print(len(directions))
    currentNode="AAA"
    i=0
    steps=0
    
    while(currentNode!="ZZZ"):
        
        #print("i",i)
        #print("currentNode",currentNode)
        #print("moving",directions[i])
        steps+=1
        currentNode = network[currentNode][int(directions[i])]
        i=(i+1)%(len(directions))
    
    print("steps",steps)
        