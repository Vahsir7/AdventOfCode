input_file_path = r"D:\Coding\AdventOfCode\2023\dec6input.txt"
with open (input_file_path, "r",encoding="utf-8") as file:
    line=file.readline().strip()
    times = int("".join(line[line.index(":")+1:].strip().split()))
    line=(file.readline().strip())
    distance =int("".join(line[line.index(":")+1:].strip().split()))
    start=end=0
    mul=1
    #print("highscore",distance[i])
    #print("Given time",time)
    for j in range(1,times):
        #print("time",j,"distance",(time-j)*j)
        if((times-j)*j>distance):
            start=j
            break
    #print("start",start)
    for j in range(times-1,0,-1):
        #print("time",j,"distance",(time-(j))*j)
        if((times-j)*j>distance):
            end=j+1
            break
    #print("end",end)    
    print(end-start)