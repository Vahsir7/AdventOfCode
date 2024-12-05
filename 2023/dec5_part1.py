input_file_path = r"D:\Coding\AdventOfCode\2023\dec5.txt"
with open (input_file_path, "r",encoding="utf-8") as file:
    s = file.readline().strip()
    #print(s)
    seeds=s[s.index(":")+1:].split()
    seeds=[int(i) for i in seeds]
    #print(seeds)
    s=file.readline().strip()
    index=file.tell()
    flag=False
    for i,seed in enumerate(seeds):
        #print("seed",seed)
        for line in file:
            
            if(line[0].isalpha()):
                #print(line)
                flag=True
    
            else:
                
                if(line!="\n"):
                    #print("lin",line)    
                    values = line.split()
                    #print("val",values)
                    a, b, r = map(int, values)
                    if(b<=seed<=(b+r) and flag==True):
                        #print(f"yes {seed} is in range {a} {a+r}")
                        seed=(a-b)+seed
                        #print("seed",seed)
                        flag=False
        seeds[i]=seed
        file.seek(index)
        #print("****************")
        #print(seeds)
        #print("****************")
    print(min(seeds))